# def add(a, b):
#     return a + b
#
# addition = add
#
# print(addition(3, 6))


# def add(a, b):
#     return a + b
#
#
# def operate(a, b, func):
#     return func(a, b)
#
#
# print(operate(3, 6, add))


# def func1():
#     c =4
#
#
#     def func2():
#         return c
#
#     return func2()
#
# def plus(a):
#     def func(b):
#         return a + b
#
#     return func
#
# add_5 = plus(5)
#
# print(add_5)
#
# print(add_5(7))

# print(func1())
# print(operate(3, 6, add))


# def print_decorator(func):
#     def wrapper():
#         print("About to be decorated")
#         func()
#         print("Just decorated")
#
#     return wrapper
#
# @print_decorator
# def printer():
#     print("I am a printer")
#
# printer()


# def print_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("About to be decorated")
#         value = func(*args, **kwargs)
#         print("Just decorated")
#         return value
#
#     return wrapper
#
#
# @print_decorator
# def printer():
#     return "I am a printer"
#
#
# @print_decorator
# def factorial(num: int) -> int:
#     import math
#     return math.factorial(num)
#
#
# # printer = print_decorator(printer)
#
# print(printer())
# print(factorial(5))



