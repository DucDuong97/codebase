def keyword_lower_onespace(t, context, report):
    violated = False
    keyword = t.value.split()[0]
    violated = violated or any(c.isupper() for c in keyword)

    exceptions = ['else', 'isset', 'unset', 'exit']
    if t.value not in exceptions:
        violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)] != ' '
        violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)+1] == ' '
    
    result = {}
    result['violated'] = violated
    result['message'] = 'Keyword must be in lowercase. There is one space after. Found: {}'.format(t.value)
    result['lineno'] = t.lexer.lineno
    return result