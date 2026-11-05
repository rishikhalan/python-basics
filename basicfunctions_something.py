def add():
    a = int(input('give me a number: '))
    b = int(input('give me a number: '))
    c = a+b
    print(c)

def sub():
    a = int(input('give me a number: '))
    b = int(input('give me a number: '))
    c = a-b
    print(c)

def mul():
    a = int(input('give me a number: '))
    b = int(input('give me a number: '))
    c = a*b
    print(c)

def div():
    a = int(input('give me a number: '))
    b = int(input('give me a number: '))
    c = a/b
    print(c)

def sq():
    a = int(input('give me a number: '))
    c = a*a
    print(c)


print("Calculator app")
while True:
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square\n6. Quit')
    choice = int(input('Give me the option you wish to choose(1-6): '))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sq()
    elif choice == 6:
        print('Quitting app...')
        break
    else:
        print('Invalid input.')



