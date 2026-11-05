sum = 0
for num in range(1,11):
    sum = sum + num
print(sum)

print("------------------------")

pro = 1

for num in range(1,11):
    pro = pro * num
print(pro)

print("-------------------")


fact = 1
nums = int(input("Give me a number: "))
for num in range(1,nums + 1):
    fact = fact * num
print(fact)