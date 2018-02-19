import re
import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

EmailRegex = re.compile(r'@\w+')

mo = EmailRegex.sub('@CENSORED', text)

print(mo)