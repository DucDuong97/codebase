def php_scope(report, context):
    message = ''
    violated = False
    
    if report['tokens'][0] != 'PHP_START':
        violated = True
        message = 'PHP starting tag missing'

    if report['tokens'][-1] != 'PHP_END':
        violated = True
        message = 'PHP closing tag missing'
    
    if violated:
        print("""
            ------------------------
            PARSE RULE
            violate: php_scope
            file: {}
            message: {}
        """.format(context['file'], message))