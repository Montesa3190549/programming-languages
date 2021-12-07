#Merge two sets
setA = []
setB = []
setC = []

sizeA = int(input("Enter size for setA: "))
for i in range(sizeA):
    setA.append(int(input("Enter a value: ")))

sizeB = int(input("Enter size for setB: "))
for j in range(sizeB):
    setB.append(int(input("Enter a value: ")))

#Merge set
setC.append(setA)
setC.append(setB)

print("Merged Set:", setC)