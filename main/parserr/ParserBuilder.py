import sys, inspect
import types

import yacc

class ParserBuilder(object):

    def __init__(self, lang, checkers={}):
        self.lang = lang
        # List of token names.   This is always required
        self.checkers = checkers | {}
        pass
    
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
    

    # Build the lexer
    def build(self, module, ast_module, **kwargs):

        self.parser = yacc.yacc(module=module)

        oldParse = self.parser.parse

        def newParse(ignored, input=None, lexer=None, debug=False, tracking=False):
            ast = oldParse(input, lexer, debug, tracking)
            ast_module.traverse(ast, self.checkers)
            return ast

        # replace bark with new_bark for this object only
        self.parser.parse = types.MethodType(newParse, self.parser)
        return self.parser
