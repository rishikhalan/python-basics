w=float(input("Give me ur weight :) (btw kg): "))
h=float(input("Give me ur height (heheheheh meters btw): "))
bmi=w / (h*h)
print(f"ur bmi is: {bmi}")
if bmi<18.5:
    print("eat up u are underweight.😊")
elif bmi>=18.5 and bmi<=24.9:
    print("ggs u are normal healthy person 👌👌😊😊😎😎")
elif bmi>=25 and bmi<=29:
    print("u r overweight")
elif bmi>=30 and bmi<=39.9:
    print("cut down on the junk food. u r overweight.🍟🍟🍕🍕🍕🍕")
else:
    print("start fasting, appease god, only he can help you, you morbidly obese person🙏🙏🙏🙏🙏")