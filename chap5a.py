birthdays = {'Dylan': 'Dec 3', 'Banda': 'Dec 4'}

while True:
    name = input('Enter a name or type \'blank\' to quit: ')
    if name =='blank':
        break
    if name in birthdays:
        print(name + 'is born on' + birthdays[name])
    newbday = input('Birthday not found. What is their birthday?')
    birthdays[name] = newbday
    print('Birthday database updated')
        