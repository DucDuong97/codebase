
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
        module = __import__('rules.'+self.lang, fromlist=[rule])
        self.checkers[pattern].append(getattr(getattr(module, rule), rule))
    
    def addRules(self, pattern, rules=[]):
        for rule in rules:
            self.addRule(pattern, rule)
    
    def addParseRules(self, rules=[]):
        for rule in rules:
            module = __import__('rules.'+self.lang+'.parse', fromlist=[rule])
            self.parse_rules.append(getattr(getattr(module, rule), rule))


    # Build the lexer
    def build(self,**kwargs):
        self.tokens = tuple(self.checkers)
        self.lexer = lex.lex(module=self, **kwargs)


    def context(self, context):
        self.lexer.context = context


    def getReport(self):
        return self.report


    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            self.report['tokens'].append(tok.type)
        
        for checker in self.parse_rules:
            checker(self.report, self.lexer.context)
        


    # Test it output
    def testFile(self, file_name=None):
        if file_name is None:
            if self.lexer.context is None:
                return
            file_name = self.lexer.context['file']
        else:
            self.lexer.context['file'] = file_name
        
        with open(file_name) as f:
            content = f.read()
            self.test(content)


    # Test it output
    def testTempFiles(self):
        shutil.copytree(self.lexer.context['code_dir'], self.TEMP_DIR)
        
        try:
            # the code that may cause an exception
            result = list(Path(self.TEMP_DIR).rglob("*."+self.lang))
            for file_name in result:
                self.testFile(file_name)
                self.reset()
        finally:
            # the code that always executes
            shutil.rmtree(self.TEMP_DIR)


    def reset(self):
        self.report['total_lines'] += self.lexer.lineno
        self.lexer.lineno = 0
        self.report['tokens'] = []