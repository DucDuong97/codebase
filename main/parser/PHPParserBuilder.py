from Lexer import Lexer

class PHPLexerBuilder(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('php', {
            'PHP_START':[], 'PHP_END':[],

            'PAREN_BRACE':[], 'COMMENT':[],'COMMENT_MULTILINE':[], 'STRING_DOUBLE':[], 'STRING_SINGLE':[],

            'LPAREN':[],'RPAREN':[],'LBRACE':[],'RBRACE':[],'LBRACKET':[],'RBRACKET':[],'SEMICOLON':[],'COMMA':[],'EQ':[],'NOT':[],

            'UN_OPS':[],'BIN_OPS':[],'ARROW':[],'DOUBLE_ARROW':[],

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

    def t_PHP_START(self,t):
        r'^<\?php'
        return t
    
    def t_PHP_END(self,t):
        r'\?>'
        return t

    def t_COMMENT(self,t):
        r'//.*'
        return t
    
    def t_COMMENT_MULTILINE(self,t):
        r'/\*([\s\S]*?)\*/'
        t.lexer.lineno += t.value.count('\n')
        return t
    
    def t_STRING_DOUBLE(self,t):
        r'"([\s\S]*?)"'
        t.lexer.lineno += t.value.count('\n')
        return t
    
    def t_STRING_SINGLE(self,t):
        r"'([\s\S]*?)'"
        t.lexer.lineno += t.value.count('\n')
        return t
    
    def t_ARROW(self,t):
        r'->'
        return t
    
    def t_DOUBLE_ARROW(self,t):
        r'=>'
        return t
    
    def t_LPAREN(self,t):
        r'\('
        return t
    
    def t_RPAREN(self,t):
        r'\)'
        return t
    
    def t_LBRACE(self,t):
        r'\['
        return t
    
    def t_RBRACE(self,t):
        r'\]'
        return t
    
    def t_LBRACKET(self,t):
        r'\{'
        t.lexer.block = 0
        return t
    
    def t_RBRACKET(self,t):
        r'\}'
        return t
    
    def t_SEMICOLON(self,t):
        r';'
        return t
    
    def t_COMMA(self,t):
        r','
        return t
    
    def t_UN_OPS(self,t):
        r'\+\+|--|\*\*'
        return t
    
    def t_BIN_OPS(self,t):
        r'\+=|-=|\+|-|\*|\/|\*\*|!=|!==|===|==|>=|<=|>|<|\|\||&&'
        return t
    
    def t_NOT(self,t):
        r'!'
        return t
    
    def t_EQ(self,t):
        r'='
        return t

    ############ keyword ############

    def t_IF(self,t):
        r'[i|I][f|F]\b'
        t.lexer.block = 1
        return t

    def t_FOR(self,t):
        r'[f|F][o|O][r|R]\b'
        t.lexer.block = 1
        return t

    def t_WHILE(self,t):
        r'[w|W][h|H][i|I][l|L][e|E]\b'
        t.lexer.block = 1
        return t

    ############ naming ############

    def t_CLASS_NAME(self,t):
        r'class\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['class_name'].add(t.value.split()[1])
        return t

    def t_VAR_NAME(self,t):
        r'\$[a-zA-z0-9-_]*\b'
        self.report['var_name'].add(t.value[1:])
        return t

    def t_FUNC_NAME(self,t):
        r'function\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['func_name'].add(t.value.split()[1])
        return t

    def t_CONST_NAME(self,t):
        r'const\s[a-zA-Z_][a-zA-Z0-9_]*'
        self.report['const_name'].add(t.value.split()[1])
        return t