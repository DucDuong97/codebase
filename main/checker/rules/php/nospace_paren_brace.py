def nospace_paren_brace(t):
    if len(t.value)>2:
        print("""
            ------------------------
            violate: nospace_paren_brace
            line: {}
            file: {}
        """.format(t.lineno, t.lexer.context['file']))