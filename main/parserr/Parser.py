

import yacc

class Parser(object):

    def __init__(self):
        pass


    # rule: token, callback
    def addRule(self, pattern, rule):
        pass
    

    # Build the lexer
    def build(self, module, lexer, **kwargs):
        self.parser = yacc.yacc(module=module)
        
        print(type(lexer))
        self.parser.lexer = lexer

        return self.parser
