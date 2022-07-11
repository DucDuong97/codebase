
import os
import sys
from pathlib import Path
import shutil
import types

import lex

class Lexer(object):

    TEMP_DIR = os.path.join(Path(__file__).parent,'files','temp')

    def __init__(self, lang, checkers={}, report={}):
        self.lang = lang
        # List of token names.   This is always required
        self.checkers = checkers | {}
        self.report = report | {
            'tokens':[],
            'total_lines':0,
        }
        self.parse_rules = []


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

        oldToken = self.lexer.token

        def newToken(inner_self):
            tok = oldToken()
            if not tok:
                return None
            if tok.type not in inner_self.checkers:
                return tok
            for checker in inner_self.checkers[tok.type]:
                tok.lexer = inner_self
                checker(tok)
            inner_self.lasttok = tok.type
            return tok

        # replace bark with new_bark for this object only
        self.lexer.token = types.MethodType(newToken, self.lexer)
        self.lexer.checkers = self.checkers
        self.lexer.lasttok = None
        return self.lexer
