
import os
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.insert(1, os.path.join(root_dir))
sys.path.insert(1, os.path.join(root_dir, 'lexer'))
sys.path.insert(1, os.path.join(root_dir, 'parserr'))

import lexer.lex as lex
from lexer.Factory import LexerFactory
from parserr.Factory import ParserFactory

class Checker(object):

    def __init__(self, level='parse', report={}):
        self.level = level
        
        self.report = report | {
            'total_lines':0,
        }

    def getReport(self):
        return self.report

    
    def check(self,data):
        """
        If the level is lex, run the lexer on the data, otherwise run the parser on the data
        
        :param data: the string to be parsed
        :return: The parse tree.
        """
        if self.level == 'lex':
            lex.runmain(self.lexer, data)
            return
        [ast, report] = self.parser.parse(data, lexer=self.lexer)
        self.report = report
        self.report['total_lines'] = self.lexer.lineno
        
    
    def checkContext(self, context):
        self.context = context

        self.lexer = LexerFactory.getLexer(self.context['lang'], self.context)
        print(self.lexer.lineno)
        if self.level == 'parse':
            self.parser = ParserFactory.getParser(self.context['lang'], self.context)
        
        if context is None:
            return
        file_name = context['file']
        
        with open(file_name) as f:
            content = f.read()
            self.check(content)


    def reset(self):
        self.report['total_lines'] += self.lexer.lineno
        self.lexer.lineno = 1
        self.report['tokens'] = []
