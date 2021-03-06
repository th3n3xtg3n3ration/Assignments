"""
Task : Print the Fizz Buzz numbers.

Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.

Print numbers from 1 to 100 inclusively following these instructions:
    1. if a number is multiple of 3, print "Fizz" instead of this number,
    2. if a number is multiple of 5, print "Buzz" instead of this number,
    3. for numbers that are multiples of both 3 and 5, print "FizzBuzz",
    4. print the rest of the numbers unchanged.

Output each value on a separate line.
"""
maximum= int(input("Please enter a maximum number in range: "))

def fizzbuzz(maximum):
    for i in range(1,maximum):
        if (i % 15) == 0:
            print("Fizz")
            continue
        elif (i % 3) == 0:
            print("Buzz")
            continue
        elif (i % 5) == 0:
            print("FizzBuzz")
            continue
        else:
            print(i)
            continue

def main():
    fizzbuzz(maximum)

if __name__ == "__main__":
    main()