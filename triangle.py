import sys
sys.path.append('/repo_mcmct')
import math
from colorama import Fore
from colorama import Style
import numpy as np
import matplotlib.pyplot as plt 
import utililty_MM as functions

t = True
z = True

title = "\nWelcome to McMcT Project :-)"
print(Fore.GREEN + title.upper())
print(Style.RESET_ALL)


while t:
    if t:
        x_a = float(input("\ninsert point A coordinate:""\n\n""x_a = "))
        y_a = float(input("y_a = "))
        x_b = float(input("insert point B coordinate:""\n""x_b = "))
        y_b = float(input("y_b = "))
        x_c = float(input("insert point C coordinate:""\n""x_c = "))
        y_c = float(input("y_c = "))
        
        p = np.array([[x_a, y_a], [x_b, y_b], [x_c, y_c]])
        c = ['pink', 'red', 'green']

        plt.figure()
        plt.scatter(p[:, 0], p[:, 1], color = c[1])

        t1 = plt.Polygon(p[:, :], color = c[0])
        plt.gca().add_patch(t1)
        plt.savefig("Triangle.pdf")
        plt.show()
        plt.close()

        t = False

        _ab = (x_a - x_b) ** 2 + (y_a - y_b) ** 2
        side_ab = math.sqrt(_ab)
        _bc = (x_b - x_c) ** 2 + (y_b - y_c) ** 2
        side_bc = math.sqrt(_bc)
        _ac = (x_a - x_c) ** 2 + (y_a - y_c) ** 2
        side_ac = math.sqrt(_ac)

    if t == False:
        if side_ab + side_bc > side_ac and side_ab + side_ac > side_bc and side_ac + side_bc > side_ab:
            print("\nvery good,this is triangle\n")
            main = True

        else:

            print("\nOops,this is not triangle,please insert coordinates again")
            t = True

while main:
    print("\nlets go\n\nWhat would you like to count?")
    insert_ = input(
        "\n for Perimeter-insert perimeter please\n for area - insert area please\n for angles - insert angles\n for length insert length please\n for stop insert stop please\n ")

    perimeter1 = functions.perimeter_func(side_ab, side_bc, side_ac)
    
    area1 = functions.area_func(side_ab, side_bc, side_ac, perimeter1)
    
    angle1 = functions.angle_func(side_ab, side_bc, side_ac)  
    
    if insert_ == "perimeter":
        perimeter_ = perimeter1
        perimeter_ = round(perimeter_, 2)
        print("\nPerimeter is ", perimeter_)
    elif insert_ == "area":
        
        area_ = functions.area_func(side_ab, side_ac, side_bc, perimeter1)
        area_ = round(area_, 2)
        print("\narea is ", area_)
    elif insert_ == "length":
        side_ab = round(side_ab, 2)
        side_bc = round(side_bc, 2)
        side_ac = round(side_ac, 2)
        print("\nAB = ", side_ab, "\nBC = ", side_bc, "\nAC = ", side_ac)
    elif insert_ == "angles":
        angle = angle1
        ang_a = round(angle[0], 2)
        ang_b = round(angle[1], 2)
        ang_c = round(angle[2], 2)

        print("\nAngle A is", ang_a)
        print("\nAngle B is", ang_b)
        print("\nAngle C is", ang_c)
        z == False
    elif insert_ == "stop":
        break
        
    else:
          print("\nPlease insert correct!")
