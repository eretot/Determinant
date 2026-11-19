print("Siseta lineearfunktsioon")
a11 = float(input("a11: ").replace(",", "."))
a12 = float(input("a12: ").replace(",", "."))
v1 = float(input("Vabaliige v1: ").replace(",", "."))
a21 = float(input("a21: ").replace(",", "."))
a22 = float(input("a22: ").replace(",", "."))
v2 = float(input("Vabaliige v2: ").replace(",", "."))


def multiply(a, b):
    return a * b

def calc(a11, a12, v1, a21, a22, v2):
    x1 = multiply(a11, a22)
    y1 = multiply(a12, a21)
    D = x1 - y1


    x2 = multiply(v1, a22)
    y2 = multiply(v2, a12)
    Dx = x2 - y2 


    x3 = multiply(a11, v2)
    y3 = multiply(a21, v1)
    Dy = x3 - y3

    x = Dx / D
    y = Dy / D

    
    print(f'x = {x}')
    print(f'y = {y}')

calc(a11, a12, v1, a21, a22, v2)
