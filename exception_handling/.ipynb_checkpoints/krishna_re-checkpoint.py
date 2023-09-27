def substitute(Pattern,replace,arg):
    n=""
    for i in arg:
        if i not in Pattern:
            n+=i
        else:
            n+=replace
    print(n)