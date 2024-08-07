height = input ("enter your height in m: ")
weight = input ("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = round(bmi, 1)
if bmi_as_int <= 18.9:
     print(f"Your BMI {bmi_as_int} Underweight")
elif bmi_as_int < 25: 
    print(f"Your BMI {bmi_as_int} Normal") 
elif bmi_as_int  < 30: 
    print(f"Your BMI {bmi_as_int} Overweight")
elif bmi_as_int < 35: 
    print(f"Your BMI {bmi_as_int} Obese")             
else:
    print(f"Your BMI {bmi_as_int} Extremly obese")