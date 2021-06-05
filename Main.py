from Parser import parseFile
from sys import argv

def main(file):
    parseFile(file)

if __name__ == "__main__":
    main(argv[1])