
import os
import sys
import time
from pathlib import Path


root_dir = Path(__file__).parent
sys.path.insert(1, os.path.join(root_dir,'checker'))

from Factory import LexerFactory


lang = sys.argv[1]
lang_dir = sys.argv[2]

lexer = LexerFactory().getLexer(lang)
if not lexer:
    print("ARG ERROR: invalid language type")
    sys.exit()

lexer.context({ "code_dir": lang_dir })

start_time = time.time()
lexer.testTempFiles()
exec_time = time.time() - start_time

print()
print('***********')
print('REPORT')
print('***********')
print('total lines:', lexer.report['total_lines'])
print('Execution time:', exec_time, 'seconds')
print('class names:', lexer.report['class_name'])
print()
print('function names:', lexer.report['func_name'])
print()
print('variable names:', lexer.report['var_name'])
print()