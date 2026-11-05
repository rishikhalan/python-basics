attendance = float(input("What is your attendance rate? "))
if attendance >= 75:
    print("Good job! You can appear for your finals. (❁´◡`❁)")
else:
    reason = input("Was it medical(y/n)?")
    if reason == "y":
        print("Hope you get better soon. You can appear for your finals. (❁´◡`❁)")
    else:
        print("I feel bad. You can't appear for your finals. T-T")