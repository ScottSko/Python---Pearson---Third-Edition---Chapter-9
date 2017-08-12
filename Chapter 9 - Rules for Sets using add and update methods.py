def main():

    #When you create the set, it must be defined with an iterable item. For a string, it will iterate each character in the string, including the space.
    #You cannot pass integers when you are defining the set, since they are not iterable items.
    #If you define the set and use a list of items, you can create the set with the literal strings rather than the characters of the string.
    #You can also define the set with numbers if you pass them via a list.

    #When you use the .add method, you can add one item at a time. You are allowed to pass strings and numbers.
    #Using the .add method, strings will be treated as the full strings, NOT JUST THE INDIVIDUAL CHARACTERS.
    #You do not need to pass a list using the .add method to get a full string or number.
    #You cannot pass lists via the .add method.

    #For the .update method, it works the same as when you define the list. Using .update to add a string will add each individual character, not the full string.
    #Since it works the same as when you define the list, you can only pass iterable items via the .update method. e.g., you cannot pass numbers via the .update method.
    #You can pass lists via the .update method.

    myset = set("hello")
    myset.update("1")
    print(myset)

main()