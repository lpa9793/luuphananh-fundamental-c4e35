#calculate BMI
weight_kg=float(input("Enter your weight (kg): "))
height_cm=float(input("Enter your height (cm): "))
height_m=height_cm/100
BMI=weight_kg/(height_m*height_m)

print("You are ", end="")

if BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")
