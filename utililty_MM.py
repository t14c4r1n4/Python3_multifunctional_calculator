import math

def perimeter_func(a, b, c):
        perimeter_ = a + b + c
        return perimeter_
def area_func(a, b, c, p):

        area_1 = (p/2) * (p/2 - a) * (p/2 - b) * (p/2 - c)
        area_ = math.sqrt(area_1)
        return area_

def angle_func(a, b, c):
        angle1 = (c ** 2 + b ** 2 - a ** 2) / (2 * c * b)
        angle_a = math.acos(angle1)
        angle2 = (c ** 2 + a ** 2 - b ** 2) / (2 * c * a)
        angle_b = math.acos(angle2)
        angle3 = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
        angle_c = math.acos(angle3)
        return angle_a, angle_b, angle_c
    