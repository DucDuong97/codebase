

from .phplexer.PHPLexerBuilder import PHPLexerBuilder
from .phplexer.phplex import reserved as php_keywords, assignments as php_assignments, bin_ops as php_bin_ops, un_ops as php_un_ops
from .jslexer.JSLexerBuilder import JSLexerBuilder
from .csslexer.CSSLexerBuilder import CSSLexerBuilder

class LexerFactory(object):

    @staticmethod
    def getLexer(lang, context={}):
        if lang == 'php':
            return LexerFactory.buildPHPLexer(context)
        if lang == 'js':
            return LexerFactory.buildJSLexer(context)
        if lang == 'css':
            return LexerFactory.buildCSSLexer(context)
        return False

    @staticmethod
    def buildPHPLexer(context):
        builder = PHPLexerBuilder()

        builder.setContext(context)

        builder.addRule('LPAREN', 'lparen_nospace')
        builder.addRule('RPAREN', 'rparen_nospace')
        builder.addRules('LBRACE', ['lbracket_nospace', 'nospace_paren_brace'])
        builder.addRule('RBRACE', 'rbracket_nospace')
        builder.addRule('SEMI', 'semicolon_nospace')
        builder.addRule('COMMA', 'comma_space')

        # m.addRuleOnGroup(php_assignments, 'binops_nospace')
        # m.addRuleOnGroup(php_bin_ops, 'binops_nospace')

        builder.addRule('BOOLEAN_NOT', 'unops_nospace')
        builder.addRuleOnGroup(php_un_ops, 'unops_nospace')

        builder.addRuleOnGroup(php_keywords, 'keyword_lower_onespace')

        return builder.build()


    @staticmethod
    def buildJSLexer(context):
        builder = JSLexerBuilder()

        builder.setContext(context)

        return builder.build()


    @staticmethod
    def buildCSSLexer(context):
        builder = CSSLexerBuilder()

        builder.setContext(context)

        return builder.build()