class getBMI:
    weight = 0
    height = 0
    def solve(**kwargs):
        return (kwargs['val1'] / kwargs['val2']**2) * 10000

    def getWeight():
        getBMI.weight = float(input("Enter your weight in kg: "))
    
    def getHeight():
        getBMI.height = float(input("Enter your height in cm: "))
    def category(bmi):
        if bmi < 18.5 : return "You are Underweight"
        elif bmi >= 18.5 and bmi < 25 : return "You are Normal Weight"
        elif bmi >= 25 and bmi < 30 : return "You are Overweight"
        elif bmi >= 30 and bmi < 35 : return "You are Class I Obesity"
        elif bmi >= 35 and bmi < 40 : return "You are Class II Obesity"
        else: return "You are Class III Obesity"

bmi = getBMI
bmi.getWeight()
bmi.getHeight()
bmiVal = round(bmi.solve(val1=bmi.weight, val2=bmi.height), 2)
print(f"Your BMI is: {bmiVal}")
print(bmi.category(bmiVal))