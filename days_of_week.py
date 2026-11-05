day=input("Give me the day of the week: ")
if day == "Monday":
    print("Start of the work week!")
elif day == "Friday":
    print("Almost weekend!")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Just another weekday.")