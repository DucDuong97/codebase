
import sys, inspect

from ParserBuilder import ParserBuilder
from . import phpparse
from . import phpast



class PHPParserBuilder(ParserBuilder):
    
    def __init__(self):
        clsmembers = inspect.getmembers(sys.modules[phpast.__name__], inspect.isclass)
        asts = [i[0] for i in clsmembers]
        super().__init__('php', dict.fromkeys(asts, []))

    def build(self):
        return super().build(phpparse, phpast)