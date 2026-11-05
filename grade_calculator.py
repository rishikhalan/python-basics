print("enter score for 3 subjects: ")
eng=int(input())
Sci=int(input())
maths=int(input())
total= eng + Sci + maths
avr= total/3 
print(f"average score = {avr}")
if avr>= 95:
    print("you got A")
elif avr>= 90 and avr<= 95:
    print("you got B")
elif avr>=75 and avr<= 90:
    print("you got C(lucky pass)")
else:
    print("you got D, disowned ") 