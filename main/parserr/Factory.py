
from .phpparser.PHPParserBuilder import PHPParserBuilder
from .jsparser.JSParserBuilder import JSParserBuilder

class ParserFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def getParser(lang, context={}):
        if lang == 'php':
            return ParserFactory.buildPHPParser(context)
        if lang == 'js':
            return ParserFactory.buildJSParser(context)
        if lang == 'css':
            return ParserFactory.buildCSSParser(context)
        return False

    @staticmethod
    def buildPHPParser(context):
        m = PHPParserBuilder()

        m.setContext(context)

        m.addRule('Class', 'classname_pascal')
        m.addRule('Method', 'funcname_camel')

        variable_group = ['Variable', 'FormalParameter']
        m.addRuleOnGroup(variable_group, 'varname_snake')

        return m.build()


    @staticmethod
    def buildJSParser(context):
        m = JSParserBuilder()

        m.setContext(context)

        return m.build()


    @staticmethod
    def buildCSSParser(context, report):
        m = JSParserBuilder()

        m.setContext(context)
        m.setReport(report)

        return m.build()