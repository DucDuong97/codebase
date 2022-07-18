def unops_nospace(t, context, report):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos+1] == ' '
    result = {}
    result['violated'] = violated
    result['message'] = 'Unary operator: NO space after. Found: {}'.format(t.value)
    return result