def make_shirt (size='l', color='red', text='i love py'):
    print(f"Your shirt is :\n{size.title()} {color.title()} \nText:{text.title()}")
make_shirt('m', 'red', ' ')
make_shirt(size='m', color='red', text=' ')
make_shirt()
make_shirt('m', 'black', 'I know lang')