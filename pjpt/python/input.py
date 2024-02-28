#!/bin/python3

x = float(input("Give me a number: "))
o = input("Give me an operator: ").strip()
y = float(input("Give me yet another number: "))

match o:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case _:
        print("Unknown operator.")
