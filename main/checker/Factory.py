

from PHPLexer import PHPLexer

class LexerFactory(object):
    def __init__(self):
        pass

    def getLexer(self, lang):
        if lang == 'php':
            return self.buildPHPLexer()
        if lang == 'js':
            return self.buildJSLexer()
        if lang == 'css':
            return self.buildCSSLexer()
        return False

    def buildPHPLexer(self):
        m = PHPLexer()

        m.addRule('LPAREN', 'lparen_nospace')
        m.addRule('RPAREN', 'rparen_nospace')
        m.addRules('LBRACKET', ['lbracket_nospace', 'nospace_paren_brace'])
        m.addRule('RBRACKET', 'rbracket_nospace')
        m.addRule('SEMICOLON', 'semicolon_nospace')
        m.addRule('COMMA', 'comma_space')
        m.addRule('UN_OPS', 'unops_nospace')
        m.addRule('BIN_OPS', 'binops_nospace')

        m.addRule('CLASS_NAME', 'classname_pascal')
        m.addRule('FUNC_NAME', 'funcname_camel')
        m.addRule('VAR_NAME', 'varname_snake')

        m.addRule('IF', 'keyword_lower_onespace')
        m.addRule('FOR', 'keyword_lower_onespace')
        m.addRule('WHILE', 'keyword_lower_onespace')

        m.build()

        return m