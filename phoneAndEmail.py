# Script that picks out phone numbers and email addresses from the contents of the clip board
# It returns the parsed phone and email addresses to the clip board

import sys
import pyperclip, re

print(sys.version)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))  # area code 3 digits, or 3 digits in brackets
    (\s|-|\.)?          # optional separator of space, - , or . 
    (\d{3})             # first three digits of 
    (\s|-|\.)?          # separator
    (\d{2,5})           # between 3 and 5 digits
    )''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})''', re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste()) # 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print(text)
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups)

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print ('Copied to clipboard:')
    print ('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')