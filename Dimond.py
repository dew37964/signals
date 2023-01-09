print("THE DIAMOND EXPERT SYSTEM")
q1 = input("Does it float in water?(Y/N)  ")
if q1 == 'Y' :
    print('Fake')
else:
    q2 = input("Does it scratch glass? (Y/N)")
    if q2 == 'N' :
        print('Fake')
    else:
        q3 = input("Does it conduct Electricity? (Y/N)")
        if q3 == "Y":
            print("Fake")
        else :
            print("Could be real.")
