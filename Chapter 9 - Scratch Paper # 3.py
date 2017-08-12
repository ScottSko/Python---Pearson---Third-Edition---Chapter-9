def main():

    new_file = open("file_analysis.txt", "w")
    new_file2 = open("file_analysis2.txt", "w")

    new_file.write("I am here. Hello World Beautiful Weather")
    new_file2.write("I am here. Hi Earth Lovely Day")

    new_file.close()
    new_file2.close()

main()