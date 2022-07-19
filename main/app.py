import sys
import time

from checker.Checker import Checker
from structure_analyser.AppAnalyser import AppAnalyser

dir = sys.argv[1]

print('***********')
print('ANALYZING')
structure_analyser = AppAnalyser(dir)

constexts = structure_analyser.getContexts()
print('FINISH ANALYZING')
print('***********')
print()

m = Checker(level='parse')

start_time = time.time()
for context in constexts:
    m.checkContext(context)
    
    report = m.getReport()

    print()
    print('***********')
    print('REPORT')
    print('***********')
    print('file:', context['file'])
    print('total lines:', report['total_lines'])
    print()
    print('class names:', report['class_name'])
    print()
    print('function names:', report['func_name'])
    print()
    print('variable names:', report['var_name'])
    print('***********')

exec_time = time.time() - start_time
print('Execution time:', exec_time, 'seconds')