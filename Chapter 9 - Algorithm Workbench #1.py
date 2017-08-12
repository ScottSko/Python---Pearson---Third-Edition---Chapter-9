def main():

    dict = {"Jim" : 1, "James" : 2}

    print(dict)

    if "Jim" in dict:
        del dict["Jim"]
    else:
        print("Not contained")
    print(dict)

main()