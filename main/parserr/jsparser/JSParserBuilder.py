
from ParserBuilder import ParserBuilder
from . import jsparser



class JSParserBuilder(ParserBuilder):
    
    def __init__(self):
        # List of token names.   This is always required
        pass

    def build(self):
        return super().build(jsparser)