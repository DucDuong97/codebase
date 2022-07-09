
import os
import sys
from pathlib import Path

from Lexer import Lexer
root_dir = Path(__file__).parent
sys.path.insert(1, os.path.join(root_dir,'csslexer'))
import csslexer.csslexer

class CSSLexer(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('css', dict.fromkeys({}, []))


    def build(self):
        super().build(csslexer())


if '__main__' == __name__:
    
    from Factory import LexerFactory

    # Build the lexer
    m = LexerFactory().buildCSSLexer()

    context = {}
    context['file'] = 'files/test.css'
    m.context(context)
    m.checkFile()
