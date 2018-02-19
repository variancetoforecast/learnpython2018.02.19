import pyperclip

action = input('Type paste to print contents of your clipboard')

if action == 'paste':
    print(pyperclip.paste())
    

