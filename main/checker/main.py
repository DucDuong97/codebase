

from Lexer import Lexer
from PHPLexer import PHPLexer
from Factory import LexerFactory

# Build the lexer
m = LexerFactory().buildPHPLexer()

context = {}
context['file'] = 'files/test.php'
m.context(context)
m.testFile()
