def substitute(Pattern,replace,arg):
    n=""
    for i in arg:
        if i not in Pattern:
            n+=i
        else:
            n+=replace
    print(n)

def split_krishna(pattern,string1):
    cont=[]
    cont_demo=[]
    string=""
    lenth=len(pattern)
    for i in string1:
        for j in string1:
            if len(string)==len(pattern):
                cont_demo.append(string)
                string=""
                break
            else:
                string=string+j
        string1 = string1[len(pattern) - (len(pattern) - 1):]
    str2=""
    for i in cont_demo:
        if i !=pattern:
            str2=str2+i[0]
        else:
            cont.append(str2)
            str2=""
    else:
        cont.append(str2)
    print(cont)