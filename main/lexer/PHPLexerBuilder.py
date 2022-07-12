from Lexer import Lexer
import phplexer.phplex as phplex


class PHPLexerBuilder(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('php', dict.fromkeys(phplex.tokens, []))

    def build(self):
        return phplex.lexer