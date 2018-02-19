import random

def TossCoin(HeadsOrTails):
    if HeadsOrTails == 1:
        return 'Dylan'
    if HeadsOrTails == 2:
        return 'Mark'

print(TossCoin(random.randint(1,2)))

