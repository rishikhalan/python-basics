for num in range(1,67):
    if num % 5 == 0 and num % 3 == 0:
        break
    print(num)


print("------------------")
for num in range(1,50):
    if num % 5 == 0 and num % 3 == 0:
        continue
    print(num)