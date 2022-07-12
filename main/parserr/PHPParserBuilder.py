
from Parser import Parser
import phpparser.phpparse as phpparse



class PHPParserBuilder(Parser):
    
    def __init__(self):
        # List of token names.   This is always required
        pass

    def build(self, lexer):
        return super().build(phpparse, lexer)