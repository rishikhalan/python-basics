import math 
def square():
    s = float(input('give me the side: '))
    a = s*s
    p = s*4
    print(f"Area is {a}")
    print(f"Perimeter is {p}")

def rectangle():
    l = float(input('give me the length: '))
    w = float(input('Give me the width'))
    a = l*w
    p = (l+w)*2
    print(f"Area is {a}")
    print(f"Perimeter is {p}")


def circle():
    r = float(input("Enter the radius: "))
    pi = math.pi
    a = pi*r*r
    p =2*pi*r
    print(f"Area is {a}")
    print(f"Circumference is {p}")
while True:
    choice = int(input("Which operation do you want to use?(1-3)"))
    if choice == 1:
        square()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        circle()
    else:
        break
































    