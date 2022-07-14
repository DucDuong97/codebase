

from LexerBuilder import LexerBuilder
from . import csslexer

class CSSLexerBuilder(LexerBuilder):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('css', dict.fromkeys({}, []))


    def build(self):
        return super().build(csslexer.csslexer())
