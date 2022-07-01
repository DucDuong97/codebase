
import os
import sys
from pathlib import Path

root_dir = Path(__file__).parent
sys.path.insert(1, os.path.join(root_dir,'checker'))

from Factory import LexerFactory

lexer = LexerFactory().buildPHPLexer({ "code_dir": "../subfile" })

lexer.testTempFiles()

