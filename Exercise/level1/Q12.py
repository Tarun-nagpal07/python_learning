'''Build a simple shopping list program. Let the user add items, remove items, and display the
full list. Run until the user types 'quit'.'''

import time
ls = []

def insert():
    ele = input("Enter to add item : ")
    ls.append(ele)
    print("Added Successfully")

def remove():
    try:
        ele = input("Enter Item to remove : ")
        ls.remove(ele)
        print("Removed Successfully")
    except ValueError:
        print("There is no such value exits..")

def display():
    print("All list of Items : ")
    for i in ls:
        print(i)

while True:
    print("Enter 1 for insert , 2 for remove , 3 for display and 4 for exit..........")
    n = int(input("Enter your choice : "))
    match n:
        case 1:
            insert()
        case 2:
            remove()
        case 3:
            display()
        case 4:
            print("Existing..")
            time.sleep(1)
            exit()
        case _:
            print("Wrong Choice")

