def main():

    total = 0

    c_q = {"USA" : "D.C.", "England" : "London", "Australia" : "Canberra"}

    print(c_q)

    for x in c_q:
        print("What is the capital of", x, "? ")
        answer = input()
        if answer == c_q[x]:
            print("Correct!")
            total += 1
        else:
            print("Incorrect.")

    print("You got", total, "out of", len(c_q), "answers correct.")

main()