tempC=float(input("Enter a temperature in Celcius that you want convert into fahrenheit: "))
f=(tempC * 1.8 )+32 
print(f"Temp in Fahrenheit = {f:.1f}")

print("-----------------")

l=float(input("Give me the length of a rectangle: "))
w=float(input("Give me the width of a rectangle: "))
a=l * w
p=l + l + w + w
print("The area is=>" ,a)
print("The perimeter is=>" ,p)

print("-----------------")

pi=3.14
radius=float(input("Enter the radius of a circle: "))
c=2 * pi * radius
ar=pi * radius * radius
print("The area is=>" ,ar)
print("The circumfrence is=>" ,c)

print("-----------------")

pr=float(input("Give me the principle: "))
roi=float(input("Give me the rate of interest:"))
time=float(input("Give me the time(yr): "))
si=(pr * roi * time)/100
print(f"Here is your SI(simple interest): {si}")

print("----------------------------------------------------------")
uncube=int(input("Give me a number you want cubed: "))
cube=uncube**3
print(cube)