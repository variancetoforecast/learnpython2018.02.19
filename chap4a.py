print ('Enter the names of your cars. Type Finished to stop')

CarNames = []

while True:
    Name = input('Type in the name of car ' + str(len(CarNames) + 1))
    if Name == 'Finished':
        break
    CarNames = CarNames + [Name]

for Name in CarNames:
    print(Name)