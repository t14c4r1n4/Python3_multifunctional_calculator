import sys
sys.path.append('/repo_mcmct')
import math
import matplotlib as mlp
import matplotlib.pyplot as plt
import utility_TvA as ut
import numpy as np

#This is a program
#print("""Dies ist ein Programm zur Nullstellenberechnung der quadratischen Gleichungen der Form ax2+bx+c=0, c ist eine Konstante, a und b die Koeffizienten des quadratischen und linearen Glieds, d ist ebenfalls eine Konstante """)
#input coefficients

a = float(input("Eingabe des Koeffizienten für das quadratische Glied a: "))
b = float(input("Eingabe des Koeffizienten für das lineare Glied b: "))
c = float(input("Eingabe der Konstanten c: "))
d = float(input("Eingabe der Konstanten d: "))


print("Deine Gleichung lautet: \n", a, "x^2+",b ,"x+",c ,"=",d)
#quadratische Funktionen 
if a != 0:
    if  b == 0 and c == 0 and d == 0:
        x_1 = 0
        x_2 = 0
        print("0 ist eine doppelte Nullstelle")
        
    elif b == 0 and c != 0 :
        result = ut.quadratic_without_linearx(a, c, d)
        x_1, x_2 = result
        print("Die Nullstellen sind",x_1,",",x_2)
        
    elif b != 0: 
        result = ut.normal_form_zero_points(a, b, c, d)
        x_1, x_2 = result
        print(("Die Nullstellen sind",x_1,",",x_2))

#lineare Funktion lösen und Nullstelle:
elif a == 0 and b!=0:
    solve = input("Do you want to solve a linear equation (<solve_x>) \n or do you want to calculate the zeropoint of the linear equation(<zero>): ")
    if solve == "solve_x":
        x_1 = ut.linear_function_solver(b, c, d)
        x_2 = x_1
        print("Die Lösung nach x ist", x_1)
    elif solve == "zero":
        x_1 = ut.linear_function_zero_point(b, c, d)
        x_2 = x_1
        print("Die Nullstelle der linearen Funktion ist", x_1)
        
# Konstante Funktion
elif a == 0 and b == 0 and c != 0 :
    print("Die Funktion ist eine Konstante")
    if d >= 0:
        x_1 = c - d
    else:
        x_1 = c + d
    x_2 = x_1
    
save_=input("do you want to save this graph? Give it a name: ")   

# Grafik
if x_1 >= x_2:
    x = np.linspace((x_2-5),(x_1+5),100)
else:
    x = np.linspace((x_1-5),(x_2+5),100)
    
y = ut.your_function(x, a, b, c, d)
plt.plot(x, y, color = "forestgreen")

# Ein gepunktetes Diagramm-Gitter einblenden:
plt.grid(True)
# Diagramm anzeigen:
plt.savefig(save_+".pdf")
plt.show()
plt.close()