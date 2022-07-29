river = "Mississippi"
target = input('Input a character to find: ')
for index,letter in enumerate(river):
    if letter == target:
        print("Letter found at index: ", index)
        break
    else:
        print("Letter",target,'not found in',river)


s = "I love tola"
a,b,c = s.split()
print(a)
print(b)
print(c)


s = ("i love tola")
print(s.split(" "))


s = ("i love tola")
print(s.partition(" "))

def celsius_to_fahrenheit(celsius_float):
    return celsius_float * 1.8 + 32

fahrenheit: float = celsius_to_fahrenheit(100)
print(fahrenheit)






