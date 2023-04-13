pet_0={'name':'konsul', 'type':'dog', 'Host':'Ilya',}
pet_1={'name':'Jam', 'type':'cat', 'Host':'Vlad'}
pet_2={'name':'mish', 'type':'mraz', 'Host':'Sofa'}
pets=[pet_0, pet_1, pet_2]
for pet in pets[0:3]:
    print(pet['type'])
    full_name=(f"{pet['name']}",
   f"{pet['Host']}")
    print(full_name)