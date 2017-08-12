def main():

    new_file = open("encryption.txt", "r")

    dict = {}

    counter = 0

    #Goes through the whole line and returns it as a string.
    word = new_file.readline()

    #Iterates through each character in the string.

    #for x in word:
    #    print(x)

    #print(word)

    #Goes through the string and splits it into a list, which can then be used to iterate through each word.
    split = word.split()

    #print(split)

    #Iterates through each word in the list.
    
    #for x in split:
    #    print(x)

    for x in split:
        for y in split:
            if x == y:
                counter += 1
        dict[x] = counter
        counter = 0

    new_file.close()

    print(dict)

main()

