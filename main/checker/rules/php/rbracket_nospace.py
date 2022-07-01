def rbracket_nospace(t):
    violated = False
    i = 1
    while True:
        if t.lexer.lexdata[t.lexpos-i] == ' ':
            i+=1
            continue
        if t.lexer.lexdata[t.lexpos-i] != '\n' and t.lexer.lexdata[t.lexpos-i] != '\t':
            violated = True
        break
    if violated:
        print("""
            ------------------------
            violate: rbracket_nospace
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))