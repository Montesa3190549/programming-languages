class exam:
    #Parse string
    def parse(input):
        list = input.split(",")
        return list

    #Addition Function
    def add(*args):
        answer = 0
        for i in args:
            try:
                answer += int(i)
            except Exception as error:
                print("Cannot add this value: ", error)
        return answer

    #Subtract Function
    def subtract(*args):
        answer = int(args[0])
        for i in args:
            try:
                if args[0] == i:
                    continue
                answer = answer - int(i)
            except Exception as error:
                print("Cannot subtract this value: ", error)
        return answer

print("Select Operator to use:")
print("1 - Add")
print("2 - Subtract")
operator = input("Choice: ")
data = exam.parse(input("Enter series of numbers: "))
if operator == "1":    
    print(exam.add(*data))
elif operator == "2":
    print(exam.subtract(*data))
else:
    print("Invalid Input")