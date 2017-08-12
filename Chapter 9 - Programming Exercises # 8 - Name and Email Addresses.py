import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def get_menu_choice():
    print()
    print("Names and Email Addresses")
    print("-------------------------")
    print("1. Look up an address")
    print("2. Add an address")
    print("3. Change an address")
    print("4. Delete an address")
    print("5. Quit")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice

def look_up(names):

    name = input("Enter a name: ")

    print(names.get(name, "Not found."))

def add(names):

    name = input("Enter a name: ")
    address = input("Enter an email address: ")

    if name not in names:
        names[name] = address
    else:
        print("That entry already exists.")

def change(names):

    name = input("Enter a name: ")

    if name in names:
        address = input("Enter the new address: ")

        names[name] = address
    else:
        print("That name is not found")

def delete(names):

    name = input("Enter a name: ")

    if name in names:
        del names[name]
    else:
        print("That name is not found.")

def main():

    input_file = open("names.dat", "rb")
    pb = pickle.load(input_file)

    print(pb)

    names = {"Scott" : "May", "Mariel" : "June"}

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(pb)
        elif choice == ADD:
            add(pb)
        elif choice == CHANGE:
            change(pb)
        elif choice == DELETE:
            delete(pb)

    output_file = open("names.dat", "wb")
    pickle.dump(pb, output_file)
    output_file.close()

main()