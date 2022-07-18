import re

def constant_upper(node, context, report):
    violated = False
    result = {}
    # print('var_name',node,'violated',violated)
    if not isinstance(node.name, str):
        result['violated'] = violated
        return result
    const_name = node.name[1:]
    violated = violated or not re.compile("(^[A-Z])[Z-Z0-9_]*").match(const_name)
    
    report['const_name'].append(const_name)
    result['violated'] = violated
    result['message'] = 'Constant must be UPPERCASE seperable by underscore. Found name: {}'.format(const_name)
    return result