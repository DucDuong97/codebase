from Lexer import Lexer

class PHPLexer(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('php', {
            'PAREN_BRACE':[], 'COMMENT':[],'COMMENT_MULTILINE':[],

            'LPAREN':[],'RPAREN':[],'LBRACE':[],'RBRACE':[],'LBRACKET':[],'RBRACKET':[],

            'IF':[],'FOR':[],'ELSE':[],'WHILE':[],

            'CLASS_NAME':[],
            'VAR_NAME':[],
            'FUNC_NAME':[],
            'CONST_NAME':[],
        }, {
            'class_name': set(),
            'func_name': set(),
            'var_name': set(),
            'const_name': set(),
        })

    def t_COMMENT(self,t):
        r'//.*'
        return t
    
    def t_COMMENT_MULTILINE(self,t):
        r'/\*([\s\S]*?)\*/'
        return t
    
    def t_PAREN_BRACE(self,t):
        r'\)[\s]*\{'
        for checker in self.checkers['PAREN_BRACE']:
            checker(t)
        return t

    ############ keyword ############

    def t_IF(self,t):
        r'[i|I][f|F]\b'
        for checker in self.checkers['IF']:
            checker(t)
        return t

    ############ naming ############

    def t_CLASS_NAME(self,t):
        r'class\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['class_name'].add(t.value.split()[1])
        for checker in self.checkers['CLASS_NAME']:
            checker(t)
        return t

    def t_VAR_NAME(self,t):
        r'\$[a-zA-z0-9-_]*\b'
        self.report['var_name'].add(t.value[1:])
        for checker in self.checkers['VAR_NAME']:
            checker(t)
        return t

    def t_FUNC_NAME(self,t):
        r'function\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['func_name'].add(t.value.split()[1])
        for checker in self.checkers['FUNC_NAME']:
            checker(t)
        return t

    def t_CONST_NAME(self,t):
        r'const\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['const_name'].add(t.value.split()[1])
        for checker in self.checkers['CONST_NAME']:
            checker(t)
        return t
