pali = str(input("Enter a String to check for Palindrome Syndrome : ").lower())

if pali == "".join(reversed(pali)).lower():
    print("It is suffering from the Palindrome Syndrome")
else:
    print("It is not suffering from the Palidrome Syndrome")