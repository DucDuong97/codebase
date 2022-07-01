def eq_nospace(t):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(t.value)] != ' '
    if violated:
        print("""
            ------------------------
            violate: eq_nospace
            value: {}
            line: {}
            file: {}
        """.format(t.value, t.lexer.lineno, t.lexer.context['file']))