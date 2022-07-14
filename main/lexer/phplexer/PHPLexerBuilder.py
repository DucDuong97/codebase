from LexerBuilder import LexerBuilder
from . import phplex


class PHPLexerBuilder(LexerBuilder):
    
    def __init__(self):
        # List of token names.   This is always required
        report ={
        }
        checkers = {}
        for token in phplex.tokens:
            checkers[token] = []
        super().__init__('php', checkers=checkers, report=report)

    def build(self):
        lex = phplex.FilteredLexer(super().build(phplex))
        
        lex.lasttok = None
        lex.context = self.context

        return lex