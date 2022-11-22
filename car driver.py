age = int(input("Enter your age: "))
if age < 25:
     print("Hight")
else:
    type_car = input("Fast Car, Finally Car?(fast/fam) ")
    if type_car == "fam":
        print("low")
    else:
        accident = input("Had an accident?(Yes/No)")
        if accident == "Yes":
             print("high")
        else:
            accident == "No"
            print("medium")
