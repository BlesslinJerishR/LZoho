import string

abc = "".join(string.ascii_uppercase)
# print(abc)

inverse = str.maketrans(abc, abc[::-1], ' ')
word = input("Enter a word for inversion : ")
inverted = word.upper().translate(inverse)
print("The inverted word is : ", inverted)
