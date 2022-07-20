
from main.checker.Checker import Checker

m = Checker(level='parse')

m.checkContext({
    'file': 'files/test.css',
    'lang': 'css'
})