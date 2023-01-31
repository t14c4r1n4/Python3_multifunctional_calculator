def vecInput():
    xCoordA = int(input("Bitte geben Sie die x-Koordinate von Vektor a ein: "))
    yCoordA = int(input("Bitte geben Sie die y-Koordinate von Vektor a ein: "))
    xCoordB = int(input("Bitte geben Sie die x-Koordinate von Vektor b ein: "))
    yCoordB = int(input("Bitte geben Sie die y-Koordinate von Vektor b ein: "))
    veclistA = [xCoordA, yCoordA]
    veclistB = [xCoordB, yCoordB]
    return veclistA, veclistB

# Addition Vektor 2D
def vecAdd2D(veclistA,veclistB):
    vecResult = []                                       ##
    res0 = veclistA[0] + veclistB[0]
    vecResult.insert(0, res0)
    res1 = veclistA[1] + veclistB[1]
    vecResult.insert(1, res1)
    return vecResult

# Subtraktion Vektor 2D
def vecSub2D(veclistA,veclistB):
    vecResult = []
    res0 = veclistA[0] - veclistB[0]
    vecResult.insert(0, res0)
    res1 = veclistA[1] - veclistB[1]
    vecResult.insert(1, res1)
    return vecResult

def vec2D(veklist):
    vecResult = []
    vec2Dstr = '''
    \u3033'''+ str(vecResult[0]) +'''\u3035
    \u3035'''+ str(vecResult[1]) +'''\u3033
    '''
    print(vec2Dstr)