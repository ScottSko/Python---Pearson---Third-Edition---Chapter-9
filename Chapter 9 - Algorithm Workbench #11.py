import pickle

def main():

    dct = {"Scott" : 1, "Mariel" : 1}

    outputfile = open("testpickle.dat", "wb")

    pickle.dump(dct, outputfile)

    outputfile.close()

main()