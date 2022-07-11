
import os
import sys
from pathlib import Path

from Lexer import Lexer
import csslexer.csslexer as csslexer

class CSSLexerBuilder(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('css', dict.fromkeys({}, []))


    def build(self):
        super().build(csslexer.csslexer())


if '__main__' == __name__:
    
    from Factory import LexerFactory

    # Build the lexer
    m = LexerFactory().buildCSSLexer()

    context = {}
    context['file'] = 'files/test.css'
    m.context(context)
    m.checkFile()
