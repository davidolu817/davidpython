# def sub(a: int = 0, b: int =0) -> int:
#     """Calculate the difference between two values"""
#     return b - a
#
# print(sub(b = 10, a = 15))
# print(sub.__annotations__)
# print(sub.__doc__)
#
# def avg(*numbers):
#     from statistics import mean
#     return  sum(numbers) / len(numbers)
#     return mean(numbers)
# print(avg(1,2,3,4))
# print(avg(1,2,3))
#
# lst = [1,2,3,4,5]
# set_ = {1,2,3,4,5}
#
# print(avg(*lst, *set_))



# def add(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "=====>", v)
#
#     d = dict(b=6,c=5,a=7)
#     print(d)
#     # print(add(**d))
# add(b=6, c=5, a=7)

#
# def add(a, *args, b=0, **kwargs):
#     print(a)
#     print(args)
#     print(b)
#     print(kwargs)
#
# add(5, 6, 7, 8, b=9, c=0, f=8, y=4)
#
#
# def add(a, b, /, *, c):
#     print(a, b, c)
#
# add(6, 9, c=8)

# # pycharm debugger
# a = 6
# b = 8
#
# def add(x, y):
#     return x - y
#
# print(add(a, b))



 # python debugger
# import pdb
# a = 6
# b = 8
#
# def add(a, b):
#     import pdb; pdb.set_trace()
#     c =  a - b
#     return c
#
# print(add(a, b))


# def tell_me_about(a_language: str) --> str:
#     languages = ("Java", "Python", "JavaScript")
#
#     assert a_language in languages, f"Language '{a_language}' not found"
#
#     return a_language

