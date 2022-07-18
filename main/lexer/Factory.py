

from .phplexer.PHPLexerBuilder import PHPLexerBuilder
from .phplexer.phplex import reserved as php_keywords, assignments as php_assignments, bin_ops as php_bin_ops, un_ops as php_un_ops
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

        m.addRule('LPAREN', 'lparen_nospace')
        m.addRule('RPAREN', 'rparen_nospace')
        m.addRules('LBRACE', ['lbracket_nospace', 'nospace_paren_brace'])
        m.addRule('RBRACE', 'rbracket_nospace')
        m.addRule('SEMI', 'semicolon_nospace')
        m.addRule('COMMA', 'comma_space')

        # m.addRuleOnGroup(php_assignments, 'binops_nospace')
        # m.addRuleOnGroup(php_bin_ops, 'binops_nospace')

        m.addRule('BOOLEAN_NOT', 'unops_nospace')
        m.addRuleOnGroup(php_un_ops, 'unops_nospace')

        m.addRuleOnGroup(php_keywords, 'keyword_lower_onespace')
        
        return m.build()


    @staticmethod
    def buildJSLexer(context):
        m = JSLexerBuilder()

        m.setContext(context)

        return m.build()


    @staticmethod
    def buildCSSLexer(context):
        m = CSSLexerBuilder()

        m.setContext(context)

        return m.build()