
import os
import sys
from pathlib import Path
import shutil

root_dir = Path(__file__).parent.parent
sys.path.insert(1, os.path.join(root_dir))
sys.path.insert(1, os.path.join(root_dir, 'lexer'))
sys.path.insert(1, os.path.join(root_dir, 'parserr'))

import lexer.lex as lex
from lexer.Factory import LexerFactory
from parserr.Factory import ParserFactory

class Checker(object):

    TEMP_DIR = os.path.join(Path(__file__).parent,'files','temp')

    def __init__(self, context={}, level='parse', report={}):
        self.lang = context['lang']
        self.level = level
        self.context = context

        self.lexer = LexerFactory.getLexer(self.lang, context, report)
        if level == 'parse':
            self.parser = ParserFactory.getParser(self.lang, context)
        
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
        self.report.update(report)
        self.report['total_lines'] = self.lexer.lineno
        
    
    def checkFile(self, file_name=None):
        """
        It opens a file, reads the contents, and then passes the contents to the check function
        
        :param file_name: the name of the file to be checked
        :return: The return value is a list of dictionaries. Each dictionary contains the following
        keys:
        """
        if file_name is None:
            if self.context is None:
                return
            file_name = self.context['file']
        else:
            self.lexer.context = {}
            self.lexer.context['file'] = file_name
        
        with open(file_name) as f:
            content = f.read()
            self.check(content)


    # Test it output
    def checkTempFiles(self):
        shutil.copytree(self.lexer.context['code_dir'], self.TEMP_DIR)
        
        try:
            # the code that may cause an exception
            result = list(Path(self.TEMP_DIR).rglob("*."+self.lang))
            for file_name in result:
                self.checkFile(file_name)
                self.reset()
        finally:
            # the code that always executes
            shutil.rmtree(self.TEMP_DIR)


    def reset(self):
        self.report['total_lines'] += self.lexer.lineno
        self.lexer.lineno = 1
        self.report['tokens'] = []


if '__main__' == __name__:
    
    m = Checker('php')
    m.checkFile('../../files/test.php')
