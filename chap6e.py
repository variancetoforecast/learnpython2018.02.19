from sys import argv

script, passwordsearch = argv

import pyperclip

#Test if user has inputed the password input. Remember that argv[0] is the script name.abs

if len(sys.arv) < 2:
    print('Program requires two argvs')
    sys.exit

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt','luggage': '12345'}

action = PASSWORDS.get(passwordsearch, 0)

pyperclip.copy(action)

print('You have searched for ' + passwordsearch + ' ...now copied to clipboard')