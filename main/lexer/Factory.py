

from PHPLexerBuilder import PHPLexerBuilder
from JSLexerBuilder import JSLexerBuilder
from CSSLexerBuilder import CSSLexerBuilder

class LexerFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def getLexer(lang):
        if lang == 'php':
            return LexerFactory.buildPHPLexer()
        if lang == 'js':
            return LexerFactory.buildJSLexer()
        if lang == 'css':
            return LexerFactory.buildCSSLexer()
        return False

    @staticmethod
    def buildPHPLexer():
        m = PHPLexerBuilder()

        # m.addRule('LPAREN', 'lparen_nospace')
        # m.addRule('RPAREN', 'rparen_nospace')
        # m.addRules('LBRACKET', ['lbracket_nospace', 'nospace_paren_brace'])
        # m.addRule('RBRACKET', 'rbracket_nospace')
        # m.addRule('SEMICOLON', 'semicolon_nospace')
        # m.addRule('COMMA', 'comma_space')
        # m.addRule('EQ', 'eq_nospace')
        # m.addRule('NOT', 'unops_nospace')
        # m.addRule('UN_OPS', 'unops_nospace')
        # # m.addRule('BIN_OPS', 'binops_nospace')

        # m.addRule('CLASS_NAME', 'classname_pascal')
        # m.addRule('FUNC_NAME', 'funcname_camel')
        # m.addRule('VAR_NAME', 'varname_snake')

        # m.addRule('IF', 'keyword_lower_onespace')
        # m.addRule('FOR', 'keyword_lower_onespace')
        # m.addRule('WHILE', 'keyword_lower_onespace')

        # m.addParseRules(['php_scope'])

        return m.build()


    @staticmethod
    def buildJSLexer():
        m = JSLexerBuilder()

        m.addRules('LBRACE', ['nospace_paren_brace'])
        
        return m.build()


    @staticmethod
    def buildCSSLexer():
        m = CSSLexerBuilder()

        return m.build()