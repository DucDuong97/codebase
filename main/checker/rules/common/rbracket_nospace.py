def rbracket_nospace(t):
    violated = False
    i = 1
    while True:
        char = t.lexer.lexdata[t.lexpos-i]
        if char == ' ':
            i+=1
            continue
        if char != '\n' and char != '\t' and i != 1:
            violated = True
        break
    if violated:
        print("""
            ------------------------
            violate: rbracket_nospace
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))