

from LexerBuilder import LexerBuilder
from . import csslexer

class CSSLexerBuilder(LexerBuilder):
    
    def __init__(self):
        # List of token names.   This is always required
        report ={
        }
        super().__init__('css', checkers=dict.fromkeys({}, []), report=report)


    def build(self):
        return super().build(csslexer.csslexer())
