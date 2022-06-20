"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.

Write a Python program that;
    1. takes a sentence from the user,
    2. counts the number of each letter/chars of the sentence,
    3. collects the letters/chars as a key and the counted numbers as a value in a dictionary.

"""

text = input("Please enter a sentence: ")
chars = {}

def counter():
    splitter = text.split(" ")
    num_counter = text.count(" ")
    chars[" "] = num_counter
    for element in splitter:
        for i in element:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1

def main():
    counter()
    print(chars)

if __name__ == "__main__":
    main()


