
from PHPParserBuilder import PHPParserBuilder

class ParserFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def getParser(lang):
        if lang == 'php':
            return ParserFactory.buildPHPParser()
        if lang == 'js':
            return ParserFactory.buildJSLexer()
        if lang == 'css':
            return ParserFactory.buildCSSLexer()
        return False

    @staticmethod
    def buildPHPParser(lexer):
        m = PHPParserBuilder()

        return m.build(lexer)

