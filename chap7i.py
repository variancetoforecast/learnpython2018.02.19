import re
import pyperclip

text = pyperclip.paste()

print('Text copied is: \"' + text + '\"')

EmailRegex = re.compile(r'[]+@[]+(\.{2-4})')

mo = EmailRegex.findall(text)

print(mo)