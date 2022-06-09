"""
Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

The desired output is like this:

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""
# number = int(input("Please enter an integer number: "))

number = 12
first = 0
second = 1
temp = 0

number = number -2
fibonacci = []

for i in range(number):
    fibonacci += [second]
    temp = first + second
    first = second
    second = temp
    number -= 1

print(fibonacci)
