print("Fish Pond Model")
print("===============")
width = float(input("Enter pond width (meter) "))
length = float(input("Enter pond length (meter) "))
depth = float(input("Enter pond depth (meter) "))
print("\n")
print("Results")
print("-------")
area = width * length
print(area, "square meters")


volume = area * depth
print(volume, "cubic meters of water")


fish = int(volume * 2)
print('Number of fish: ', fish)