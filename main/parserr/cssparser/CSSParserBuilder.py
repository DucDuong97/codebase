
from ParserBuilder import ParserBuilder
from . import cssyacc
from . import cssast



class CSSParserBuilder(ParserBuilder):
    
    def __init__(self):
        report = {
        }
        checkers = {}
        for item in cssast.getNodeList():
            checkers[item] = []
        super().__init__('css', checkers=checkers, report=report)

    def build(self):
        return super().build(cssyacc.cssparser())