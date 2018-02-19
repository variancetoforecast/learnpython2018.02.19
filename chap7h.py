import re
import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

EmailRegex = re.compile(r'......@')

mo = EmailRegex.findall(text)

print(mo)