age_float=float(input("Enter your age: "))

if 0 <= age_float < 34:
    print("Young")
elif 35 <= age_float < 50:
    print("Mature")
elif 51 <= age_float < 69:
    print("Middle-aged")
elif 70 <= age_float:
    print("Old")
