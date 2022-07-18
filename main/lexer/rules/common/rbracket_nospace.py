def rbracket_nospace(t, context, report):
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
    result['message'] = 'Curly braces: There is NO space after { and No space before }.'
    return result