import pickle

def main():

    again = "y"

    output_file = open("info.dat", "wb")

    while again.lower() == "y":

        save_data(output_file)

        again = input("Enter more data? (y/n): ")

    output_file.close()

def save_data(file):

    person = {}

    person["name"] = input("Name: ")
    person["age"] = input("Age: ")
    person["weight"] = input("Weight: ")

    pickle.dump(person, file)


main()