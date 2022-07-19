
import re

def varname_snake(node, context, report):
    violated = False
    result = {}
    # print('var_name',node,'violated',violated)
    if not isinstance(node.name, str):
        result['violated'] = violated
        return result
    var_name = node.name[1:]
    violated = violated or not re.compile("(^(_[a-z]|[a-z]))[a-z0-9_]*").match(var_name)
    
    report['var_name'].add(var_name)
    result['violated'] = violated
    result['message'] = 'Use lower case with underscore. Found name: {}'.format(var_name)
    return result