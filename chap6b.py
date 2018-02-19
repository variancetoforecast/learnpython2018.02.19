def CarDetails(detailslist, leftwidth, rightwidth):
    print ('Car details list'.center(20,'='))
    for k, v in detailslist.items():
        print (k.ljust(leftwidth, '-') + v.rjust(rightwidth))

detailslist1 = {'Brand': 'Toyota', 'Model': 'Hilux'}
CarDetails(detailslist1, 15, 10)
