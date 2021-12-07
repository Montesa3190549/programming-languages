choice = -1
while choice != 0:
    print("1 - Add data into the set")
    print("2 - Remove data from the set")
    print("3 - Show set")
    print("0 - Exit")
    choice = int(input("Choice: "))
    if choice == 1:
        x = int(input("How many data would you like to put? "))
        initSet = set()
        for i in range(x):
            initSet.add(input("Enter data: "))
    elif choice == 2:
        element = input("Which element would you like to remove? ")
        initSet.discard(element)
    elif choice == 3:
        print(initSet)
    elif choice == 0:
        print("Thank you for using the program")
    else:
        print("Invalid Input")

