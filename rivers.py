rivers={'nile': 'egypt', 'don': 'russia', 'missisipi': 'usa',}
for k, v in rivers.items():
    if k == 'nile':
        print(f"{k.title() } stream through {v.title()}")
    if k == 'don':
        print(f"{k.title() } stream through {v.title()}")
    if k == 'missisipi':
        print(f"{k.title() } stream through {v.title()}")
for river in rivers.keys():
    print(river.title())
for river in rivers.values():
    print(river.title())