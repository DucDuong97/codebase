def binops_nospace(t):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(t.value)] != ' '
    result = {}
    result['violated'] = violated
    return result
        