pn = int(input("Give me a number:"))
for i in range(2,pn):
    if pn % i == 0:
        print("Your number is a composite number!")
        break
    else:
        print("Your number is prime!")
        break
