# coding_data.py

coding_questions = {
    "Check Palindrome": '''num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")''',

    "Check Prime Number": '''num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")''',

    "Find Factorial": '''num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial is", fact)''',

    "Fibonacci Series": '''n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b''',

    "Check Armstrong Number": '''num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")''',

    "Check Even or Odd": '''num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")''',

    "Find GCD": '''import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD is", math.gcd(a, b))''',

    "Swap Two Numbers": '''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:", a, b)''',

    "Sort a List": '''lst = [3, 1, 5, 2, 4]
lst.sort()
print("Sorted list:", lst)''',

    "Check Neon Number": '''num = int(input("Enter a number: "))
square = num * num
sum_digits = sum(int(digit) for digit in str(square))
if sum_digits == num:
    print("Neon number")
else:
    print("Not a Neon number")''',

    "Check Spy Number": '''num = int(input("Enter a number: "))
sum_digits = 0
product_digits = 1
for digit in str(num):
    sum_digits += int(digit)
    product_digits *= int(digit)
if sum_digits == product_digits:
    print("Spy number")
else:
    print("Not a Spy number")''',
}
