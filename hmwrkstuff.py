def is_prime(num):
    if num <= 1:
        return "The number is not prime"
    elif num % 2 == 0 and num > 2 :
        return "The number is not prime"
    elif num == 2:
        return "The number is prime"
    else:
        return("The number is prime")

def even_odd(num):
    if num % 2 == 0:
        return('The number is even')
    else:
        return('Number is odd')



def factorial(num):
    fact = 1
    for i in range (1, num+1):
        fact = fact * i
    return(fact)

#Main Program
num = int(input('Give me a number: '))
print(is_prime(num))
print(even_odd(num))
print(factorial(num))