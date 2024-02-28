#!/bin/python3

from Employee import Employee

e1 = Employee("Bob", "Sales", "Director of Sales", 100000, 20)
e2 = Employee("Linda", "Executive", "CIO", 150000, 10)

print(e1.name)
print(e2.name)

print(e1.eligible_for_retirement())
