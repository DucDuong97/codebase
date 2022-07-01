def binops_nospace(t):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(t.value)] != ' '
    if violated:
        print("""
            ------------------------
            violate: binops_nospace
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))