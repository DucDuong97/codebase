
import sys, inspect

from ParserBuilder import ParserBuilder
from . import phpparse
from . import phpast



class PHPParserBuilder(ParserBuilder):
    
    def __init__(self):
        checkers = {}
        for item in phpast.getNodeList():
            checkers[item] = []
        super().__init__('php', checkers=checkers)

    def build(self):
        return super().build(phpparse)