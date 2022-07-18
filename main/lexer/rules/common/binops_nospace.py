def binops_nospace(t, context, report):
    violated = False
    violated = violated or t.lexer.lexdata[t.lexpos-1] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(t.value)] != ' '
    result = {}
    result['violated'] = violated
    result['message'] = 'Assignments & binary ops: There is one space BEFORE and one space AFTER. Found: {}'.format(t.value)
    return result
        