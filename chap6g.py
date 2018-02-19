import pyperclip

#This selects the content of your clipboard

text = pyperclip.paste()

print('Text copied is' + text)

#This is the actual program functionality

list = text.split(' ')

for i in range(len(list)):
    list[i] = ', ' + list[i]

text = ' '.join(list)
    
#This selects the output of the program and copies to the clipboard

pyperclip.copy(text)

print('Text pasted is' + text)