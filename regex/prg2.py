string="gauravparashar"

new_list=[]
for c in string:
    new_list.append(c.isalnum())

print (new_list)

print (any(new_list))
