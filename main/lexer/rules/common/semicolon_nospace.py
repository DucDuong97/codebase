def semicolon_nospace(t, context, report):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] == ' '
    result = {}
    result['violated'] = violated
    result['message'] = 'No space before semicolon'
    result['lineno'] = t.lexer.lineno
    return result