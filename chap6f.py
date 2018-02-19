import pyperclip

#This selects the content of your clipboard

text = pyperclip.paste()

#This is the actual program functionality

list = text.split('\n')

for i in range(len(list)):
    list[i] = '*' + list[i]

text = '\n'.join(list)
    

#This selects the output of the program and copies to the clipboard

pyperclip.copy(text)