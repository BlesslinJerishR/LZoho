# test@1
pali = "malayalam"

# test@2
# pali = "palindrome"

if pali.lower() == "".join(reversed(pali)).lower():
    print("It is suffering from the Palindrome Syndrome")
else:
    print("It is not suffering from the Palidrome Syndrome")