"""
Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

"""
number = int(input("Please enter an integer number: "))

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,"is not a prime number.")
            break
    else:
        print(number,"is a prime number.")
else:
   print(number,"is not a prime number.")