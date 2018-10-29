
def fun(text):
    rlt=''
    l=len(text)
    for i in range(l):
        if (text[i]=='d'):
            rlt+='p'
        else:
            rlt+=text[i]
    return rlt



print(fun('abcdefgh'))
