def lbracket_nospace(t, context, report):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos+1] == ' '
    result = {}
    result['violated'] = violated
    result['message'] = 'Curly braces: There is NO space after { and No space before }.'
    result['lineno'] = t.lexer.lineno
    return result