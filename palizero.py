string = str(input("Enter the sentence to remove palindromes : "))
string_list = string.split()
checkers = []
solution = []

for x in string_list:
    if x.lower() == "".join(reversed(x.lower())):
        print("Irukuu Ulla pali iruku")
        checkers.append(x)

for x in string_list:
    if x not in checkers:
        solution.append(x)

print(" ".join(solution))