import re
import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

PhoneNumRegex = re.compile(r'(\d\d)-(\d\d\d\d-\d\d\d\d)')

mo = PhoneNumRegex.findall(text)

print(mo)
print(mo[0])