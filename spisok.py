favorite_languages = {'Artem':'Ruby', 'Danil':'C#', 'Yarik':'Kuhnya','Gleb':'no'}
for k, v in favorite_languages.items():
    if v == 'no':
     print(f"{k.title()} , proydi test")
    else:
     print(f"{k.title()} krasava")
for k, v in favorite_languages.items():
     print(f"Favor lang to {k.title()} is a {v.title()}")
