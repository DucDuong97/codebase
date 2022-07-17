import time

from checker.Checker import Checker


# need to find a JS PLY
context={
    'file':'../files/test.php',
    'lang':'php',
    'type': 'dev',
}

m = Checker(context, level='parse')

start_time = time.time()
m.checkFile()
exec_time = time.time() - start_time

print()
print('***********')
print('REPORT')
print('***********')
print('Execution time:', exec_time, 'seconds')
print('Report:', m.getReport())
# print('class names:', lexer.report['class_name'])
# print()
# print('function names:', lexer.report['func_name'])
# print()
# print('variable names:', lexer.report['var_name'])
# print()