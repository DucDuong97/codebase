def keyword_lower_onespace(t, context, report):
    violated = False
    keyword = t.value.split()[0]
    violated = violated or any(c.isupper() for c in keyword)
    violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)+1] == ' '
    result = {}
    result['violated'] = violated
    result['message'] = 'keyword: {}'.format(t.value)
    return result