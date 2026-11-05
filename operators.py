#ARTHIMETIC OPERATORS
num=int(input("Enter a number: "))
num_2=int(input("Enter a number: "))
sum=num + num_2
sub=num - num_2
m=num * num_2
d=num / num_2
floorDiv=num // num_2#floor division will ignore the decimal values and just give the whole number
mod=num % num_2 #mod is the remainder operator
ex=num ** num_2 #exponent is num to the power of num 2
print( num, "+", num_2, "=" ,sum)

#f string
print(f"{num} - {num_2} = {sub}")
#normal
print( num, "*", num_2, "=" ,m)
#f string
print(f"{num} / {num_2} = {d:.2f}")
#normal
print( num, "/", num_2, "= %.2f" %d)
#f string
print(f"{num} // {num_2} = {floorDiv}")
print(f"{num} % {num_2} = {mod}")
print(f"{num} ** {num_2} = {ex}")

("---------")