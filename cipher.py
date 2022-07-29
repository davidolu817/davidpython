# word = input("Enter a word to encode: ")
#
# while not word.isalpha():
#     word = input("Enter a word to encode: ")
#
#     print(word)





import  string

import decipher as decipher

abc = string.ascii_lowercase
user_input = input("Enter a string to cipher")
while not user_input.isalpha():
    user_input = input("Enter a string to cipher")

    key = input("Enter a key")
if key.isdigit():
    key = int(key)
    if user_input.isalpha():
        clipher = user_input.translate(abc, abc[key:] +abc[:key])
print(clipher)

decipher + clipher.translate(str.maketrans(abc[key:] +abc[:key], abc))
print(declipher)
