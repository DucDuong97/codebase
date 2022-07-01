import re

def classname_pascal(t):
    print(t.value)
    violated = False
    class_name = t.value.split()[1]
    violated = violated or not re.compile("(^[A-Z])[a-zA-Z0-9]*").match(class_name)
    if violated:
        print("""
            ------------------------
            violate: classname_pascal
            line: {}
            file: {}
        """.format(t.lineno, t.lexer.context['file']))