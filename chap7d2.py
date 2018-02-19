import re
import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

PhoneNumRegex = re.compile(r'(\d{2})')
mo = PhoneNumRegex.search(text)
print('Phone number found: ' + mo.group())

"""PhoneNumRegex = re.compile(r'(\d{2}) \d{4}-\d{4}')"""