def swappers2x(p1,p2,leng):
    """Swapper2x
        To Swap two letters and check whether the words are
        suffering from palindrome Syndome .
    Args:
        p1 (str)    : [ Palindrome1 ]
        p1 (str)    : [ Palindrome2 ]
        len (int)   : [ Length of the word ]
    """
    A = []
    B = []
    
    for i in range(leng):
        if p1[i] != p2[i]:
            A.append(p1[i])
            B.append(p2[i])
        
    if len(A) == len(B) == 0:
        return True

    if len(A) == len(B) == 2:
        if A[0] == A[1] and B[0] == B[1]:
            return True
        
    return False 

# Driver Code
A = input("Enter the 1st word : ")
B = input("Enter the 2nd word : ")

if(swappers2x(A, B, len(A))):
    print("The words are swappable")
else:
    print("The words are not Swappable")
    