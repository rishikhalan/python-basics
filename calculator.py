num=int(input("Give me a number: "))
num_2=int(input("Give me a number: "))
op=input("Give me a operator(+, -, *, /): ")
if op == "*":
    print(f"{num} * {num_2} = {num * num_2}")

elif op == "+":
    print(f"{num} + {num_2} = {num + num_2}")

elif op == "-":
    print(f"{num} - {num_2} = {num - num_2}")

else:
    print(f"{num} / {num_2} = {num / num_2}")