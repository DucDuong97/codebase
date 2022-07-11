def nospace_paren_brace(t):
    violated = False
    if t.lexer.lasttok == 'RPAREN':
        violated = violated or t.lexer.lexdata[t.lexpos-1] != ')'
    if violated:
        print("""
            ------------------------
            violate: nospace_paren_brace
            line: {}
            file: {}
        """.format(t.lexer.lineno, t.lexer.context['file']))