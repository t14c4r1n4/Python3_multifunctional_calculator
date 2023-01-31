import sys
sys.path.append('/repo_mcmct')
from utility_MS import *

defVector = '''

Vektoren sind eindeutig durch die Angabe einer Masszahl und einer Richtung definiert.

'''  
var = 1
# optionale Parameter ??

#vecResult = []


def vec2D(veklist):
    vec2Dstr = '''
    \u3033'''+ str(vecResult[0]) +'''\u3035
    \u3035'''+ str(vecResult[1]) +'''\u3033
    '''
    print(vec2Dstr)
    

veclistA, veclistB = vecInput()
vecResult = vecAdd2D(veclistA,veclistB)
vec2D(vecResult)
vecResult = vecSub2D(veclistA,veclistB)

vec2D(vecResult)


