def comma_space(t, context, report):
    violated = False
    violated = violated or (t.lexer.lexdata[t.lexpos+1] != ' ' and t.lexer.lexdata[t.lexpos+1] != '\n')
    result = {}
    result['violated'] = violated
    result['message'] = ' There is one space AFTER comma'
    result['lineno'] = t.lexer.lineno
    return result