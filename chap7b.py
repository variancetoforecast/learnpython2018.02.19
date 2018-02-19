import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

def isphonenumber(check):
    if len(check) !=14:
        return False
    if check[0] != '(':
        return False
    if check[3] != ')':
        return False
    for i in range(5,8):
        if not check[i].isdecimal():
            return False
    for i in range(10,13):
        if not check[i].isdecimal():
            return False
    return True

isphonenumber(text)

if isphonenumber is True:
    print('Text contains a phone number')
else:
    print('Not a phone number')



