def dupes_remover(l1):
    o = ""
    dupe = []
    if len(l1) <= 4:
        for x in l1:
            if(x in o):
                dupe.append(x)
                pass
            else:
                o = x + o + '0'
        print("The Origin : ",o,end="")
        print(o)
    else:
        print("[!Buggu] --> Innu Kannu pudikala  , therinja enaku sollu kudu .")

n1 = list(input("Enter N1 : "))
dupes_remover(n1)

# @test1
# print(n1)

# Bugs Greater than 4 Digits

# Input 2:  
# 1 2 2 5 6 9 5 2  
# Output 2:  
# 1 2 0 5 6 9 0 2 
            