def rbracket_nospace(t):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] == ' '
    if violated:
        print("""
            ------------------------
            violate: rbracket_nospace
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))