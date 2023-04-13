people_1= {'first_name': 'chris' ,  'last_name' : 'Corano' , 
'sity':'Moscow','age':25 }
people_2= {'first_name':'uma','last_name':'sorensen', 
'sity': 'tula','age':32}
people_3= {'first_name':'peng', 'last_name':'feng', 
'sity':'Mahachkala','age':27}
people_4= [people_1, people_2, people_3]
for people in people_4:
   print (people)
for people in people_4[0:3]:
    print(people['sity'])
    full_name=(f"{people['first_name']}",
   f"{people['last_name']}")
    print(full_name)