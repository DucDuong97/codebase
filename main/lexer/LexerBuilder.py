
import sys
import types

import lex

class LexerBuilder(object):

    def __init__(self, lang, checkers={}, report={}):
        self.lang = lang
        # List of token names.   This is always required
        self.checkers = checkers | {}
        self.report = report

    # rule: token, callback
    def addRule(self, pattern, rule):
        if pattern not in self.checkers:
            print('invalid pattern: ', pattern)
            sys.exit()
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
    
    def addRuleOnGroup(self, group, rule):
        for pattern in group:
            self.addRule(pattern, rule)

    def addRules(self, pattern, rules=[]):
        for rule in rules:
            self.addRule(pattern, rule)

    def setContext(self, context):
        self.context = context

    # Build the lexer
    def build(self, module=None, **kwargs):
        if module == None:
            self.lexer = lex.lex(module=self, **kwargs)
        else:
            self.lexer = lex.lex(module=module, **kwargs)

        oldToken = self.lexer.token

        def violationHandler(t, result={}):
            message = ''
            if 'message' in result:
                message = result['message']
            print("""
                ------------------------
                violate: {}
                message: {}
                line: {}
                file: {}
            """.format(result['name'], message, t.lexer.lineno, t.lexer.context['file']))

        def newToken(inner_self):
            tok = oldToken()
            if not tok:
                return None
            if tok.type not in self.checkers:
                return tok
            for checker in self.checkers[tok.type]:
                # print('type', tok.type, 'checker', checker)
                tok.lexer = inner_self
                result = checker(tok, self.context, self.report)
                if result['violated']:
                    result['name'] = checker.__name__
                    violationHandler(tok, result=result)
            inner_self.lasttok = tok.type
            return tok

        # replace bark with new_bark for this object only
        self.lexer.token = types.MethodType(newToken, self.lexer)

        self.lexer.lasttok = None
        self.lexer.context = self.context
        
        return self.lexer
