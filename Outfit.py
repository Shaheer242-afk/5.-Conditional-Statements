temperature = int(input("Please enter the temperature today: "))

if temperature < 20:
    outfit = "jacket"
    print("It is a cold day. Please wear a", outfit)
else:
    outfit = "T-Shirt"
    print("It is a warm day. PLease wear a", outfit)

is_raining = input("Is it raining today? (yes/no): ")
if is_raining == "yes":
    print("Please take a umbrella today.")

wind_speed = int(input("Please enter the windspeed today: "))

if wind_speed > 30:
    wind_breaker = "yes"
    print("You need a windbreaker today")
else:
    wind_breaker = "no"
    print("You don't need a windbreaker today")

has_puddles = input("Is there any Puddles today? (yes/no)")
if has_puddles == "yes":
    shoes = "boots"
    print("Please wear", shoes, "as the ground is wet")

else:
    shoes = "sneakers"
    print("Please wear", shoes,"as the ground is dry")

print("")
print("Weather check Complete!")

print("=========WEATHER OUTFIT PICKER=========")
print("Temperature = ", temperature)
print("Outfit = ", outfit)
print("Is raining? = ", is_raining)
print("The windspeed = ", wind_speed)
print("Needs a Windbreaker = ", wind_breaker)
print("Are there Puddles? = ", has_puddles)
print("What shoes do you need = ", shoes)
print("=======================================")