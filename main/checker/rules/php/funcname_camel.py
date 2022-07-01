import re

def funcname_camel(t):
    violated = False
    func_name = t.value.split()[1]
    violated = violated or not re.compile("(^[a-z])[a-zA-Z0-9]*").match(func_name)
    if violated:
        print("""
            ------------------------
            violate: varname_snake
            line: {}
            file: {}
        """.format(t.lineno, t.lexer.context['file']))