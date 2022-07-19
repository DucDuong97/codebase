
from ParserBuilder import ParserBuilder
from . import phpparse
from . import phpast



class PHPParserBuilder(ParserBuilder):
    
    def __init__(self):
        report = {
            'class_name': set(),
            'func_name': set(),
            'var_name': set(),
            'const_name': set(),
        }
        checkers = {}
        for item in phpast.getNodeList():
            checkers[item] = []
        super().__init__('php', checkers=checkers, report=report)

    def build(self):
        return super().build(phpparse)