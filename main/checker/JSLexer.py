import os
import sys
from pathlib import Path

from Lexer import Lexer
root_dir = Path(__file__).parent
sys.path.insert(1, os.path.join(root_dir,'jslexer'))
import jslexer.jslexer

class JSLexer(Lexer):
    
    def __init__(self):
        # List of token names.   This is always required
        super().__init__('js', dict.fromkeys(jslexer.jslexer.tokens, []))


    def build(self):
        super().build(jslexer.jslexer)


if '__main__' == __name__:
    
    from Factory import LexerFactory

    # Build the lexer
    m = LexerFactory().buildJSLexer()

    context = {}
    context['file'] = 'files/test.js'
    m.context(context)
    m.checkFile()
