print("Size of pond")
print("============")
width = input("Enter pond width (meters) ")
width = float (width)
length = float(input("Enter pond length (meters) : "))
depth = float(input("Enter pond depth (meters) : "))
area = width * length
volume = area * depth
print(volume, "cubic meters of water")
print("\n")

print("Filling the pond")
print("================")
second = float(input("Enter liters per sesond: "))
hour = second * 3600
print(hour, "liters per hour")
day = hour*24
#convert liters/day to cubc meters per day (m^3=1000)
day = day/1000
print(day, "cubic meters per day")
'''
The number of days to fill the pond is the volume of the pond, divided by the water flow in one day
'''
day = volume/day
#round the number to 2 decimal palces
days = round(days,2)
print("it will take", day,"day to fill the pond")

#convert the numbers