sandwich_orders=['big', 'joe', 'extar cheese','pastrami',
'pastrami','pastrami', 'fairy dust']
finished_sandwiches=[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(f"Ready sandwich: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)
print("SANDWICH READY:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
