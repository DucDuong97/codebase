def rparen_nospace(t):
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
    result = {}
    result['violated'] = violated
    return result