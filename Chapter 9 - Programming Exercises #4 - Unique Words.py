def main():

    new_file = open("encryption.txt", "r")

    newset = set()


    for line in new_file:
        word = line.split()
        newset.update(word)

    print(newset)

    new_file.close()

main()

