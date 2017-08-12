import pickle

def main():

    inputfile = open("testpickle.dat", "rb")

    pb = pickle.load(inputfile)

    print(pb)

    inputfile.close()

main()