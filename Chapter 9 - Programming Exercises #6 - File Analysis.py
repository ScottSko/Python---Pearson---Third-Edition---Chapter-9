def main():

    new_file = open("file_analysis.txt", "r")
    new_file2 = open("file_analysis2.txt", "r")

    word1 = new_file.read()
    word2 = new_file2.read()

    file1 = word1.split()
    file2 = word2.split()

    set1 = set(file1)
    set2 = set(file2)

    new_file.close()
    new_file2.close()

    union = set1.union(set2)
    intersection = set1.intersection(set2)
    set1_difference = set1.difference(set2)
    set2_difference = set2.difference(set1)
    symmetric_difference = set1.symmetric_difference(set2)

    print(union)
    print(intersection)
    print(set1_difference)
    print(set2_difference)
    print(symmetric_difference)

main()