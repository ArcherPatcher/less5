def make_album(name='none', author='none',list='none'):
    album={'name':name, 'author':author, 'list':list}
    return album
users=[]
user=input("Ur name:")
users.append(user)
n=0
while user=='q':
    break
for user in users:
    while True:
        print("\nSelect name")
        print("Text q to quit")

        name=input("Album Name:")
        if name== 'q':
         break
        else:
            n=n+1
        author=input("Author:")
        if author=='q':
          break
        else:
            n=n+1
        list= input("List:")
        if list== 'q':
         break
        else:
            n=n+1
        if n==3:
           break
current_album=make_album(name, author, list)
print(f"\n {user} Select album: {current_album}")