cls_romm = {"name": "Ana", "age": 22}
name = cls_romm["name"]
print(f"cls_room: {name}")
# tuple
emp = {"name": "Ana", "aged": 28, "smoke": False, ("h", "w"): (6, 75)}

print("\n")
print(emp)

print(emp['smoke'])

print(emp[('h', 'w')])

# print(emp['sal'])


emp['sal'] = 10000

print(emp)


print("\n **** Opeations for a directory ****")
print(" clear()             Return True if all elements of the tuple are true ( or if the tuple is empty)")
print(" get( key [,d])      Return True if any element of the tuple is True, if the tuple is empty return False")
print(" items()             Retun an enumerate object. It contains the indez and value of all the items of tuple as pairs.")
print(" keys()              ")
print(" pop( key [,d])      Remove and return an arbitary item (key, value), Raises keyError. if the dictionary is empty ")
print(" popitem()           Return the smallest item in the tuple")
print(" update([other])     Update the dictionary with the key/value pairs from other, overwritinh existing keys")
print(" values()            Return a new view of the dictionary's values")

name = emp.get('name')
print(f"\n\n emp.get('name'): {name}")
emp.pop('sal')
print(emp)
print(f"\n\n emp.pop('sal'):  {emp}")

emp.clear()
print(emp)
print(f"\n\n emp.clear() ")

#del emp
#print(f"\n\n del emp ")

emp = {"name": "Ana", "aged": 28, "smoke": False, ("h", "w"): (6, 75)}
print(f"\n emp.keys():     {emp.keys()}")
print(f"emp.values():   {emp.values()}")
print(f"emp.items():    {emp.items()} \n")
print(emp)
emp.update({"name": "Lidia"})
print("emp.update({'name':'Lidia'})")
print(f"\n {emp}")
emp['name'] = "Ana Lidia"
print("emp['name'] = 'Ana Lidia'")
print(emp)
