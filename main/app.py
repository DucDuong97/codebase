import sys
import time

from checker.Checker import Checker
from context_analyser.AppAnalyser import AppAnalyser

dir = sys.argv[1]

print('CONTEXT ANALYZING')
print('...')
structure_analyser = AppAnalyser(dir)

contexts = structure_analyser.getContexts()
print('FINISH ANALYZING!!!!')
print()

m = Checker(level='parse')

total_lines = 0
longest_file = {
    'name': '',
    'lines': 0,
}

start_time = time.time()
for context in contexts:
    print('**********************')
    print('file:', context['actual_file'])
    print()
    print('-----------')
    print('VIOLATION')
    print('-----------')
    m.checkContext(context)
    
    report = m.getReport()

    print()
    print('-----------')
    print('REPORT')
    print('-----------')
    print('total lines:', report['total_lines'])
    print()
    if len(report['class_name']):
        print('class names:', report['class_name'])
        print()

    if len(report['func_name']):
        print('function names:', report['func_name'])
        print()

    if len(report['var_name']):
        print('variable names:', report['var_name'])
    print()
    print()
    print()

    total_lines += report['total_lines']
    if report['total_lines'] > longest_file['lines']:
        longest_file = {
            'name': context['actual_file'],
            'lines': report['total_lines'],
        }




print('**********************')
print('-----------')
print('TOTAL REPORTS')
print('-----------')

exec_time = time.time() - start_time
print('Execution time:', exec_time, 'seconds')
print('Longest file:', longest_file['name'], '. Lines:', longest_file['lines'])