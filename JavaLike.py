import lex

class JavaLike(object):
    def __init__(self):
        # List of token names.   This is always required
        self.tokens = (
            'IDE',
            'FUN', 'IF', 'FOR', 'FOREACH', 'CLASS'
            'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'LPAREN', 'RPAREN', 
            'PAREN_BRACE'
        )

    def t_IF(self,t):
        r'if\s'
        self.enter_scope = True
        return t

    def t_CLASS(self,t):
        r'class\s[a-zA-Z_][a-zA-Z0-9_]*'
        class_name = t.value.split()[1]
        print("class name: ", class_name)
        if not class_name[0].isupper():
            print("ERROR!!!")
        return t

    def t_PAREN_BRACE(self,t):
        r'\)[\s]*\{'
        if len(t.value)>2:
            print("ERROR!!!")
        return t


    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
