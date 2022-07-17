def nospace_paren_brace(t, context, report):
    violated = False
    if t.lexer.lasttok == 'RPAREN':
        violated = violated or t.lexer.lexdata[t.lexpos-1] != ')'
    result = {}
    result['violated'] = violated
    return result