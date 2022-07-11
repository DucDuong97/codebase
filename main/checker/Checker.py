
import os
import sys
from pathlib import Path
import shutil

root_dir = Path(__file__).parent.parent
sys.path.insert(1, os.path.join(root_dir,'lexer'))
import lex
from Factory import LexerFactory

class Checker(object):

    TEMP_DIR = os.path.join(Path(__file__).parent,'files','temp')

    def __init__(self, lang, report={}):
        self.lexer = LexerFactory.getLexer(lang)
        self.lang = lang
        
        self.report = report | {
            'tokens':[],
            'total_lines':0,
        }

    def setContext(self, context):
        self.context = context


    def getReport(self):
        return self.report

    # Test it output
    def check(self,data):
        lex.runmain(self.lexer, data)
        
    # Test it output
    def checkFile(self, file_name=None):
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
