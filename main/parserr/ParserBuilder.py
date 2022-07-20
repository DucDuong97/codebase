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
    
    _parser = None
    _original_parse = None
    
    # Build the parser
    def build(self, module, **kwargs):

        if ParserBuilder._parser is not None:
            ParserBuilder._parser.restart()
            parser = ParserBuilder._parser
        else:
            parser = yacc.yacc(module=module)
            ParserBuilder._parser = parser
            ParserBuilder._original_parse = parser.parse

        

        def violationHandler(node, result={}):
            message = ''
            if 'message' in result:
                message = result['message']
            print("""
                ------------------------
                violate: {}
                message: {}
                line: {}
            """.format(result['name'], message, result['lineno']))


        def newParse(ignored, input=None, lexer=None, debug=False, tracking=False):
            try:
                ast = ParserBuilder._original_parse(input, lexer, debug, tracking)
            except SyntaxError as e:
                print(str(e))
                return [False, None, None]

            def traverse(nodes, checkers):
                def visitor(node):
                    for checker in checkers[type(node).__name__]:
                        result = checker(node, self.context, self.report)
                        result['name'] = checker.__name__
                        if result['violated']:
                            violationHandler(node, result=result)
                for node in nodes:
                    try:
                        node.accept(visitor)
                    except Exception as e:
                        print(str(e))

            traverse(ast, self.checkers)
            return [True, ast, self.report]

        parser.parse = types.MethodType(newParse, parser)

        return parser
