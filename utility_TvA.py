import math


def your_function(x, a, b, c, d):
    if d == 0:
        y = a*(x**2)+b*x+c
    elif d < 0:
        y = a*(x**2)+b*x+c+d
    elif d > 0:
        y = a*(x**2)+b*x+c-d
    return y

def normal_form_zero_points(a, b, c , d):
    if d == 0:
        q = c / a
    elif d != 0 and d > 0:
        c = c - d
        q = c / a
    elif d != 0 and d < 0:
        c = c + d
        q = c / a  
    p = b / a
    if ((p / 2)**2 - q) < 0:
        result = "Es gibt keine Lösung!"
    else:
        x_1 = -(p / 2) + math.sqrt(((p / 2)**2) - q)
        x_2 = -(p / 2) - math.sqrt(((p / 2)**2) - q)
        result = (x_1, x_2)      
    return result

def quadratic_without_linearx(a, c , d):#if a!=0 and b == 0 and c != 0:
    if c > 0:
        c_1 = d - c
        const = (c_1 / a)
    elif c < 0:
        c_1 = d + c
        const = (c_1 / a )
    elif c == 0:
        const = d
    if const < 0:
        result = "Es gibt keine Lösung!"
    else: 
        x_1 = -1*math.sqrt(const)
        x_2 = math.sqrt(const) 
        result = (x_1, x_2)
    return result

def linear_function_solver(b, c, d):#elif a==0 and b != 0 and c != 0 :
    if c > 0:
        const = d - c
    elif c < 0:
        const = d + c
    elif c == 0:
        const = d
    x = const / b
    return x

def linear_function_zero_point(b, c, d):
    if d < 0:
        c_1 = c + d 
    elif d > 0:
        c_1 = c-d
    elif d == 0:
        c_1 = c
    x = c_1 / b
    return x