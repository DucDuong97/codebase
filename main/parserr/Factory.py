
from .phpparser.PHPParserBuilder import PHPParserBuilder
from .jsparser.JSParserBuilder import JSParserBuilder

class ParserFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def getParser(lang, context):
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

        return m.build()


    @staticmethod
    def buildJSParser(context):
        m = JSParserBuilder()

        m.setContext(context)

        return m.build()


    @staticmethod
    def buildCSSParser(context):
        m = JSParserBuilder()

        m.setContext(context)

        return m.build()