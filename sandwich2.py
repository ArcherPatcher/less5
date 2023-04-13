def build_profile(tall, weight, first, last, **user_ifo):
    user_ifo['Tall']=tall
    user_ifo['Weight']=weight
    user_ifo['first_name']=first
    user_ifo['last_name']=last
    return user_ifo
user_profile=build_profile(183, 85, 'aga','noga',location='moscow', field='shava', age=42)
print(user_profile)
import sandwich as s
s.make_sandwich('ham','rye')