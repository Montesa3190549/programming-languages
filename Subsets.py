#Subsets
setA = [1,2,3,4,5,6]
setB = [2,4,6]

for i in setB:
    for j in setA:
        if i == j:
            print(i, "is a subset of set A: ", setA)