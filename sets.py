setA = {1,2,3,4,5}
setB = {2,4,6,8,10}

print("Set A: ", setA)
print("Set B: ", setB)
print("Which operation would you like to use?")
print("1 - Union")
print("2 - Intersection")
print("3 - Difference")
choice = int(input("Choice: "))

if choice == 1:
    print (setA | setB)
elif choice == 2:
    print (setA & setB)
elif choice == 3:
    print (setA - setB)
else:
    print("Invalid Input")
