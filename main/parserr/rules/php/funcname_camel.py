import re

def funcname_camel(node, context, report):
    violated = False
    func_name = node.name
    violated = violated or not re.compile("(^(__[a-z]|[a-z]))[a-zA-Z0-9]*").match(func_name)

    report['func_name'].append(func_name)
    result = {}
    result['violated'] = violated
    return result