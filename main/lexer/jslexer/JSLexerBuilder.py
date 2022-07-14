
from LexerBuilder import LexerBuilder
from . import jslexer

class JSLexerBuilder(LexerBuilder):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('js', dict.fromkeys(jslexer.tokens, []))

    def build(self):
        return super().build(jslexer)


