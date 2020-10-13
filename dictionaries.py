#DICTIONARIES
"""
d1 = {}
choice = "yes"
while condition == "yes":
    key1 = input()
    value1 = input()
    d1[key1] = value1
    choice = input("Would you like to add another Contact? (yes or no): ")
    if choice == "no":
        break
print()d1
"""
d2 = {3 : "salman", 4 : "raj" , 6:"ss"}
d2[7] = "vijayawada"
print(d2)

#print(d1.keys())
#print(d1.values())
#print(d1.items())
#OPERATIONS CAN PERFORM IN DICTIONARY
"""
UPDATE : dictionaryname[key] = value
insert : dictionaryname[new key] = value
delete : dictionaryname.pop(key) or del dictionaryname[key]

dictionaryname.keys()
dictionaryname.values()
dictionary name.items()
"""
"""
clear() = d1.clear()
copy() =  new variable = d1.copy()
fromkeys() = dict.fromkeys(x , y)
get() = d1.get("key")
items() = d1.items()
keys() = d1.keys()
pop() = d1.pop("key")
popitem() = d1.popitem()
update() = d1[new key] = value
values() = d1.values()
"""