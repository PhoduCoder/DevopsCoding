max_width=4

string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"

list_new=[string[i:i+max_width] for i in range(0, len(string), max_width)]

print(list_new)

print ('\n'.join(list_new))
