def comma_space(t):
    violated = False
    violated = violated or (t.lexer.lexdata[t.lexpos+1] != ' ' and t.lexer.lexdata[t.lexpos+1] != '\n')
    result = {}
    result['violated'] = violated
    return result