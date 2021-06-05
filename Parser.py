from GP_Algos import GeneticProgram

f = None
gp = None
index = 0

def parseFile(a):
    global f
    global gp

    f = open(a, "r")
    gp = GeneticProgram()
    
    parseFunctions()

    f.close()

def parseFunctions():
    funcs = 0

    line = f.readline()
    if not line[:11] == "Functions: ":
        err("Functions: ", 1)

    try:
        funcs = int(line[11:])
    except:
        err("integer", 1)

    parseFunctionDefinitions(funcs)

def parseFunctionDefinitions(count):

    for i in range(count):
        line = f.readline()
        if not gp.addFunction(line[:len(line) - 1]):
            err("Valid function type", 2 + i)

    parseTests(count + 2)

def parseTests(ln):
    inputs = 0
    tests = 0

    line = f.readline()
    if not line[:8] == "Inputs: ":
        err("Inputs: ", ln)

    try:
        inputs = int(line[8:])
        gp.setInputs(tests)
    except:
        err("integer", ln)

    line = f.readline()
    if not line[:7] == "Tests: ":
        err("Tests: ", ln + 1)

    try:
        tests = int(line[7:])
    except:
        err("integer", ln + 1)

    parseTestCase(inputs, ln + 2, tests)

def parseTestCase(inputs, ln, count):
    for i in range(count):
        line = f.readline()
        raw = line.split(' ')
        vals = []
        if len(raw) != inputs + 1:
            err("test case with {} inputs".format(inputs), ln + i)
        try:
            vals = [int(r) for r in raw]
        except:
            err("test case with integer inputs".format(inputs), ln + i)
        gp.addTest(vals)

    gp.printAlgos()

def err(string, line):
    print("Expected line {}: \"{}\"".format(line, string))
    exit(0)