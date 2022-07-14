def unops_nospace(t):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos+1] == ' '
    result = {}
    result['violated'] = violated
    return result