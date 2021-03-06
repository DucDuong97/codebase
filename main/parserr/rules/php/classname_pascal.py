import re

def classname_pascal(node, context, report):
    violated = False
    class_name = node.name
    violated = violated or not re.compile("(^[A-Z])[a-zA-Z0-9]*").match(class_name)
    
    report['class_name'].add(class_name)
    result = {}
    result['violated'] = violated
    result['message'] = 'Use singular CamelCase. found name: {}'.format(class_name)
    result['lineno'] = node.lineno
    return result