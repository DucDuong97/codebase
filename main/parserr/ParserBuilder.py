import sys, inspect
import types

import yacc

class ParserBuilder(object):

    def __init__(self, lang, checkers={}, report={}):
        self.lang = lang
        # List of token names.   This is always required
        self.checkers = checkers
        self.report = report
        pass
    
    # rule: token, callback
    def addRule(self, pattern, rule):
        if pattern not in self.checkers:
            print('invalid pattern: ', pattern)
            sys.exit()
        try:
            module = __import__('rules.'+self.lang, fromlist=[rule])
            attr = getattr(getattr(module, rule), rule)
        except:
            try:
                module = __import__('rules.common', fromlist=[rule])
                attr = getattr(getattr(module, rule), rule)
            except:
                print('invalid rule: ', rule)
                sys.exit()
        
        self.checkers[pattern].append(attr)


    def addRuleOnGroup(self, group, rule):
        for pattern in group:
            self.addRule(pattern, rule)


    def setContext(self, context):
        self.context = context
    

    # Build the parser
    def build(self, module, **kwargs):

        self.parser = yacc.yacc(module=module)

        oldParse = self.parser.parse

        def violationHandler(node, result={}):
            message = ''
            if 'message' in result:
                message = result['message']
            print("""
                ------------------------
                violate: {}
                message: {}
                line: {}
                file: {}
            """.format(result['name'], message, node.lineno, self.context['file']))


        def newParse(ignored, input=None, lexer=None, debug=False, tracking=False):
            ast = oldParse(input, lexer, debug, tracking)

            def traverse(nodes, checkers):
                def visitor(node):
                    for checker in checkers[type(node).__name__]:
                        result = checker(node, self.context, self.report)
                        result['name'] = checker.__name__
                        if result['violated']:
                            violationHandler(node, result=result)
                for node in nodes:
                    node.accept(visitor)

            traverse(ast, self.checkers)
            return [ast, self.report]

        # replace bark with new_bark for this object only
        self.parser.parse = types.MethodType(newParse, self.parser)
        return self.parser
