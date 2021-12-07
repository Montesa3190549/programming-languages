values = input("Enter values that you want to multiply: ")
list1 = values.split(",")
ans = 1
errorLoop = False
for i in list1:
    try:
        ans = ans * int(i)
    except Exception as error:
        errorLoop = True
        break
if errorLoop == False:
    print ("Answer:", ans)
else:
    print("An invalid input has been detected")