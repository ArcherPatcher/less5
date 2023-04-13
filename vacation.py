places={}
poll=True
while poll:
    name=input("Whats ur name?")
    place=input("Where you wish goin?")
    places[name] = place
    repeat = input("would you like to let another (yes/no)")
    if repeat=='no':
      poll=False
print("\n---Poll Results---")
for name, places in places.items():
    print(f"{name} would like to drive {places}.")
