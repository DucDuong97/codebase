
import os
import sys
from pathlib import Path
import shutil

import lex

class Lexer(object):

    TEMP_DIR = os.path.join(Path(__file__).parent,'files','temp')

    def __init__(self, lang, checkers={}, report={}):
        self.lang = lang
        # List of token names.   This is always required
        self.checkers = checkers | {
            'TEST_ADD_RULE':[],'TEST_ADD_RULE_FROM_MODULE':[],
        }
        self.report = report | {
            'tokens':[],
            'total_lines':0,
        }
        self.parse_rules = []


    def t_TEST_ADD_RULE(self,t):
        r'TEST_ADD_RULE'
        for checker in self.checkers['TEST_ADD_RULE']:
            checker(t)
        return t

    def t_TEST_ADD_RULE_FROM_MODULE(self,t):
        r'TEST_ADD_RULE_FROM_MODULE'
        for checker in self.checkers['TEST_ADD_RULE_FROM_MODULE']:
            checker(t)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self,t):
        t.lexer.skip(1)


    # rule: token, callback
    def addRule(self, pattern, rule):
        if pattern not in self.checkers:
            print('invalid pattern: ', pattern)
            sys.exit()
        # get fule function
        try:
            module = __import__('rules.'+self.lang, fromlist=[rule])
            attr = getattr(getattr(module, rule), rule)
        except:
            try:
                module = __import__('rules.common', fromlist=[rule])
                attr = getattr(getattr(module, rule), rule)
            except:
                print('invalid rule: ', rule)
                sys.exit()
        
        self.checkers[pattern].append(attr)
    

    def addRules(self, pattern, rules=[]):
        for rule in rules:
            self.addRule(pattern, rule)
    
    def addParseRules(self, rules=[]):
        for rule in rules:
            module = __import__('rules.'+self.lang+'.parse', fromlist=[rule])
            self.parse_rules.append(getattr(getattr(module, rule), rule))


    # Build the lexer
    def build(self, module=None, **kwargs):
        self.tokens = tuple(self.checkers)
        if module == None:
            self.lexer = lex.lex(module=self, **kwargs)
        else:
            self.lexer = lex.lex(module=module, **kwargs)


    def context(self, context):
        self.lexer.context = context


    def getReport(self):
        return self.report


    # Test it output
    def check(self,data):
        self.lexer.input(data)
        self.lexer.lasttok = None
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok.type, tok.value)
            if tok.type not in self.checkers:
                continue
            for checker in self.checkers[tok.type]:
                tok.lexer = self.lexer
                checker(tok)
            self.lexer.lasttok = tok.type
            self.report['tokens'].append(tok.type)
        
        for checker in self.parse_rules:
            checker(self.report, self.lexer.context)
        


    # Test it output
    def checkFile(self, file_name=None):
        if file_name is None:
            if self.lexer.context is None:
                return
            file_name = self.lexer.context['file']
        else:
            self.lexer.context['file'] = file_name
        
        with open(file_name) as f:
            content = f.read()
            self.check(content)


    # Test it output
    def checkTempFiles(self):
        shutil.copytree(self.lexer.context['code_dir'], self.TEMP_DIR)
        
        try:
            # the code that may cause an exception
            result = list(Path(self.TEMP_DIR).rglob("*."+self.lang))
            for file_name in result:
                self.checkFile(file_name)
                self.reset()
        finally:
            # the code that always executes
            shutil.rmtree(self.TEMP_DIR)


    def reset(self):
        self.report['total_lines'] += self.lexer.lineno
        self.lexer.lineno = 1
        self.report['tokens'] = []