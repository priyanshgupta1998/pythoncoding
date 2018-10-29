
def encrypt(text,s):
    result=''
    l=len(text)
    for i in range(l):
        if (text[i].isupper()):
            result+= chr((ord(text[i]) + s-65) % 26 + 65)
        elif(text[i].islower()):
            result+= chr((ord(text[i]) + s - 97) % 26 + 97)
        else:
            result+=text[i]
    return result

text = "ROT13 Algorithm"
s = 13
print(encrypt(text,s))
