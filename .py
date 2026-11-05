alphabet = 'qwertyuiopasdfghjklzxcvbnm'
for letter in alphabet:
    print(f"{letter} : {ord(letter)}")


x = chr(654886)
print(x)



print('-----------------------------------------')


word = input("Word? ")



for letter in word:
    if ord(letter) >= 65 and ord(letter) <= 90:
        print(letter, end = "")
    else:
        val = ord(letter) - 32
        x = chr(val)
        print(x, end = "")

