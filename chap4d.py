spam = ['cat', 'bat', 'rat', 'elephant']

spam.insert(-1,'and')

for i in range(len(spam)):
    print(spam[i], end=', ')