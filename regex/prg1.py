import re

given_string="rabcdeefgyYhFjkIoomnpOeorteeeeet"

pattern=re.compile(r'[^AEIOUaeiou][AEIOUaeiou]{2,}[^AEIOUaeiou]')

matches=pattern.findall(given_string)

print(matches)


=======

import re

string=input()

pattern=re.compile(r'[^AEIOUaeiou][AEIOUaeiou]{2,}[^AEIOUaeiou]')

matches=pattern.findall(string)

if not matches:
    print ("-1")

for i in range(len(matches)):
    print (matches[i][1:-1])

