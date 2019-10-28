def p1():
    print("d")

def p2():
    print("9")

myDict = {
    "P1": p1,
    "P2": p2,
    
}

def myMain(name):
    myDict[name]()
    
myMain("P1")