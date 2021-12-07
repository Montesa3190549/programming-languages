def solve(**kwargs):
    return (kwargs['val1'] / kwargs['val2']**2) * 10000

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = round(solve(val1=weight, val2=height), 2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5 : print("You are Underweight")
elif bmi >= 18.5 and bmi < 25 : print("You are Normal Weight")
elif bmi >= 25 and bmi < 30 : print("You are Overweight")
elif bmi >= 30 and bmi < 35 : print("You are Class I Obesity")
elif bmi >= 35 and bmi < 40 : print("You are Class II Obesity")
else: print("You are Class III Obesity")