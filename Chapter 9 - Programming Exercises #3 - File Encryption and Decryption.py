def main():

    codes = { "A" : "%", "a" : "9", "B" : "@", "b" : "#"}

    new_file = open("encryption.txt", "w")

    new_file.write("AAA" + "\n")
    new_file.write("aaa" + "\n")
    new_file.write("BBB" + "\n")
    new_file.write("bbb" + "\n")

    new_file.close()

    encrypted_file = open("encryption.txt", "r")

    decrypted_file = open("decrypt.txt", "w")


    #The trick to the loop below is that you actually use three loops to read through the file.
    #The first loop reads each string in the file.
    #The second loop reads each character in the string.
    #The third loops compares that character to one of the entries in the dictionary.
    #If it finds a match, it writes the corresponding value to the new file.

    new_line = 0


    for x in encrypted_file:
        if new_line != 0:

            decrypted_file.write("\n")
        new_line = 1
        for y in x:
            for z in codes:
                if z == y:
                    line = codes[z]
                    decrypted_file.write(line)

    encrypted_file.close()

    decrypted_file.close()

main()