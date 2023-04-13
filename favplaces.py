fav_places={'Artem':['Spain','Moscow'], 
'Gleb':['Cypr','Kazakhstan',],
'Yarik':['london','greece'], 
'Ilya':['Nv','surgut']}
for k, v in fav_places.items():
    print(f"\n{k.title()}'s fav places are:")
    for v_1 in v:
        print(f"\t{v_1.title()}")   
