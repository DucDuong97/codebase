import re

def funcname_camel(t):
    violated = False
    func_name = t.value.split()[1]
    violated = violated or not re.compile("(^(__[a-z]|[a-z]))[a-zA-Z0-9]*").match(func_name)
    if violated:
        print("""
            ------------------------
            violate: funcname_camel
            line: {}
            file: {}
            message: {}
        """.format(t.lineno, t.lexer.context['file'], func_name))