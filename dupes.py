def dupes_remover(l1):
    o = ""
    dupe = []
    for x in l1:
        if(x in o):
            dupe.append(x)
            pass
        else:
            o = x + o + '0'
    print("The Origin : ",o)

n1 = list(input("Enter N1 : "))

# @test1
print(n1)

dupes_remover(n1)
            