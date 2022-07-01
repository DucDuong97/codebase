def comma_space(t):
    violated = False
    violated = violated or (t.lexer.lexdata[t.lexpos+1] != ' ' and t.lexer.lexdata[t.lexpos+1] != '\n')
    if violated:
        print("""
            ------------------------
            violate: comma_space
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))