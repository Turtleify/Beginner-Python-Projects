my_list = []

def view():
    print(my_list)

def add(): 
    adding = input('What would you like to add? ')
    my_list.append(adding)
    print('Okay! Just added your task to the list!')

def delete():
    print(my_list)
    deleting = input('Which task would you like to remove? Write the number of the item. ')
    i = int(deleting)
    del my_list[i - 1]

def to_do_list():
    while True:
        choice = input('What would you like to do? (1 = view, 2 = add, 3 = delete, 4 = quit) ')
        if choice == '1':
            view()
        elif choice == '2':
            add()
        elif choice =='3':
            delete()
        elif choice == '4':
            print('See ya!')
            break
        else:
            print('Please make a valid input (1, 2, 3) ')

to_do_list()