import re

def classname_pascal(t):
    violated = False
    class_name = t.value.split()[1]
    violated = violated or not re.compile("(^[A-Z])[a-zA-Z0-9]*").match(class_name)
    if violated:
        print("""
            ------------------------
            violate: classname_pascal
            line: {}
            file: {}
            message: {}
        """.format(t.lexer.lineno, t.lexer.context['file'], class_name))