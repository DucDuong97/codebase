def keyword_lower_onespace(t):
    violated = False
    keyword = t.value.split()[0]
    violated = violated or any(c.isupper() for c in keyword)
    violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)] != ' '
    violated = violated or t.lexer.lexdata[t.lexpos+len(keyword)+1] == ' '
    if violated:
        print("""
            ------------------------
            violate: keyword_lower_onespace
            line: {}
            file: {}
        """.format(t.lineno, t.lexer.context['file']))