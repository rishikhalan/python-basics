str = ("GO SWIMMING, I MEAN IT!!!!!")
print(str)

#first letter
print(str[0])

#last letter
print(str[-1])
print(str[len(str) - 1])

#swim
print(str[3:7])

#Mean
print(str[15:19])
#go
print(str[0:2])
#go
print(str[:2])
#it!!!!!
print(str[-7:])
#reverse
print(str[::-1])




print("------------------------------------")


strr = "Rishik "
print(strr * 3)
str1 = "I love Python"
newstr = str1.replace("Python", 'travelling')
print(newstr)

print('---------------------------------')

s1 = "IlovePython"
s2 = '1234567890'
s3 = 'se3ft3bc5fg5'
print(s1.isalpha())
print(s2.isdigit())
print(s3.isalnum())

s4 = 'rAnDom cASe'
print(s4.upper())
print(s4.lower())
print(s4.capitalize())
print(s4.split())
s5 = "u aint slick"
words = s5.split()
print(words)
joinedwords = ' '.join(words)
print(joinedwords)
joinedwords1 = '~~**'.join(words)
print(joinedwords1)








#PALINDRONE
#This is a historic line - 6666666666666666666666666666666666667777777777777777777777777777777777777777777
s = "A man a plan a canal Panama"
cleantext = s.replace(' ', '').lower()
print(cleantext)
if cleantext==cleantext[::-1]:
    print('palindrome')
else:
    print('...')


strrrv = input('give me a string: ')
cc = 0
v = 0
for letter in strrrv:
    if letter.isalpha():
        if letter in 'aeiouAEIOU':
            v = v+1
        else:
            cc = cc+1
print('cosonants = ',cc)
print('vowel = ',v)



strrr = input('give me a string: ')
up = 0
lc = 0
for letter in strrr:
    if letter.isalpha():
        if letter.isupper():
            up = up+1
        elif letter.islower():
            lc = lc+1
print('up = ',up)
print('lc = ',lc)
