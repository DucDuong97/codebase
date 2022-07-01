
import os
import sys
from pathlib import Path


root_dir = Path(__file__).parent
sys.path.insert(1, os.path.join(root_dir,'checker'))

from Factory import LexerFactory


lang = sys.argv[1]
lang_dir = sys.argv[2]

lexer = LexerFactory().getLexer(lang)
if not lexer:
    print("ARG ERROR: invalid language type")
    sys.exit()

lexer.context({ "code_dir": lang_dir })

lexer.testTempFiles()

