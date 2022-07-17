

from .phplexer.PHPLexerBuilder import PHPLexerBuilder
from .jslexer.JSLexerBuilder import JSLexerBuilder
from .csslexer.CSSLexerBuilder import CSSLexerBuilder

class LexerFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def getLexer(lang, context={}, report={}):
        if lang == 'php':
            return LexerFactory.buildPHPLexer(context, report)
        if lang == 'js':
            return LexerFactory.buildJSLexer(context, report)
        if lang == 'css':
            return LexerFactory.buildCSSLexer(context, report)
        return False

    @staticmethod
    def buildPHPLexer(context, report):
        m = PHPLexerBuilder()

        m.setContext(context)
        m.setReport(report)

        m.addRule('LPAREN', 'lparen_nospace')
        m.addRule('RPAREN', 'rparen_nospace')
        m.addRules('LBRACE', ['lbracket_nospace', 'nospace_paren_brace'])
        m.addRule('RBRACE', 'rbracket_nospace')
        m.addRule('SEMI', 'semicolon_nospace')
        m.addRule('COMMA', 'comma_space')
        m.addRule('EQUALS', 'eq_nospace')
        m.addRule('BOOLEAN_NOT', 'unops_nospace')

        m.addRule('IF', 'keyword_lower_onespace')
        m.addRule('FOR', 'keyword_lower_onespace')
        m.addRule('WHILE', 'keyword_lower_onespace')
        

        return m.build()


    @staticmethod
    def buildJSLexer(context, report):
        m = JSLexerBuilder()

        m.setContext(context)
        m.setReport(report)

        return m.build()


    @staticmethod
    def buildCSSLexer(context, report):
        m = CSSLexerBuilder()

        m.setContext(context)
        m.setReport(report)

        return m.build()