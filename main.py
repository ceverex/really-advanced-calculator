# really advanced calculator
import math

def add(a, b):
    answer = int(a) + int(b)
    return answer

def sub(a, b):
    answer = int(a) - int(b)
    return answer

def multiply(a, b):
    answer = int(a) * int(b)
    return answer

def divide(a, b):
    answer = int(a) / int(b)
    return answer

def sqrt(a):
    answer = math.sqrt(a)
    return answer

def sq(a):
    answer = int(a) ** 2
    return answer

def chatgpt():
    i = 0
    while i < 10:
        print("YOU CAN'T USE CHATGPT")
        i += 1

process = input("Enter math function you would like to use: ")
if process == 'sqrt':
    a = input('Enter value: ')
    ans = sqrt(int(a))
    print(ans)

elif process == 'sq':
    a = input('Enter value: ')
    ans = sq(int(a))
    print(ans)

elif process == 'chatgpt':
    chatgpt()

else:
    a = input('Enter the first value: ')
    b = input('Enter the second value: ')

    if process == 'add':
        ans = add(a, b)
        print(ans)
    elif process == 'sub':
        ans = sub(a, b)
        print(ans)
    elif process == 'multiply':
        ans = multiply(a, b)
        print(ans)
    elif process == 'divide':
        ans = divide(a, b)
        print(ans)