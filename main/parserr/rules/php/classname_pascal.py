import re

def classname_pascal(node):
    violated = False
    class_name = node.name
    violated = violated or not re.compile("(^[A-Z])[a-zA-Z0-9]*").match(class_name)
    result = {}
    result['violated'] = violated
    return result