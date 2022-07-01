import re

def varname_snake(t):
    violated = False
    var_name = t.value[1:]
    violated = violated or not re.compile("(^[a-z])[a-z0-9_]*").match(var_name)
    if violated:
        print("""
            ------------------------
            violate: varname_snake
            line: {}
            file: {}
            message: {}
        """.format(t.lineno, t.lexer.context['file'], var_name))