class GeneticProgram(object):

    funcs = [
        ["and", 2],
        ["or", 2],
        ["xor", 2],
        ["not", 1],
        ["+", 2],
        ["-", 2],
        ["*", 2],
        ["/", 2],
        ["**", 2],
        ["exp", 1],
        ["sqrt", 2],
        ["ln", 1],
        ["sin", 1],
        ["cos", 1],
        ["tan", 1]
    ]

    def __init__(self):
        self.functions = []
        self.tests = []

        super().__init__()

    def setInputs(self, number):
        self.inputs = number

    def addFunction(self, name):
        for f in self.functions:
            if f[0] == name:
                return True

        for f in self.funcs:
            if f[0] == name:
                self.functions.append(f)
                return True

        return False

    def addTest(self, vals):
        self.tests.append([vals[:len(vals) - 1], vals[len(vals) - 1]])

    def printAlgos(self):
        print("Functions:")
        for f in self.functions:
            print("  [{:5}] : {}".format(f[0].center(5), f[1]))
        print("Number of inputs: {}".format(self.inputs))
        print("Test cases:")
        for t in self.tests:
            print("{} = {}".format(t[0], t[1]))
