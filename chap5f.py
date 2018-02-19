allfamily = {'Dylan': {'cars': 3, 'bikes': 2},
             'Banda': {'cars': 2, 'bikes':3}}

allfamily2 = {'Sash': {'cars': 6, 'bikes': 8},
             'Ryan': {'cars': 2, 'bikes':3}}

def totalvehicles(names, item):
    vehiclecount = 0
    for k, v in names.items():
        vehiclecount = vehiclecount + v.get(item,0)
    return vehiclecount

print('Cars ' + str(totalvehicles(allfamily, 'cars')))
print('Cars ' + str(totalvehicles(allfamily2, 'bikes')))