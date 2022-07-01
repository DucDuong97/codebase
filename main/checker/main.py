

from Lexer import Lexer
from PHPLexer import PHPLexer

# Build the lexer
m = PHPLexer()

m.addRule('CLASS_NAME', 'classname_pascal')
m.addRule('FUNC_NAME', 'funcname_camel')
m.addRule('VAR_NAME', 'varname_snake')

m.addRule('PAREN_BRACE', 'nospace_paren_brace')
m.addRule('IF', 'keyword_lower_onespace')
m.addRule('FOR', 'keyword_lower_onespace')
m.addRule('WHILE', 'keyword_lower_onespace')

m.build()

context = {}
context['file'] = 'Controller.php'
m.context(context)
m.testFile()
print(m.getReport())
