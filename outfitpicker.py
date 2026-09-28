temp = int(input("Enter todays temperature in celsius:"))

if temp < 20:
    outfit = "jacket"
    print("it is cold today.")
    print ("wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today.")
    print ("wear a", outfit)

is_raining = input("is it raining today?(yes/no): ")
if is_raining == "yes":
    print("bring an umbrella!")

wind_speed = int(input("enter the wind spped in km/h:"))
if wind_speed < 30:
    outfit = "yes"
    print("it is windy.")
    print ("wear a", outfit)
else:
    outfit = "no"
    print("it is calom today.")
    print ("wear a", outfit)

has_puddles = input("are there puddles? (yes/no:")
if has_puddles == "yes":
    outfit = "boots"
    print("its wet.")
    print ("wear a", outfit)
else:
    outfit = "sneakers"
    print("it is dry.")
    print ("wear a", outfit)