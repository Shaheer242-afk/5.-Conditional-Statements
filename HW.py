temperature = int(input("Enter today's temperature in Celsius: "))
 
if temperature < 20:
    activity = "Stay indoor!"
    print("It is cold today.")
    print(activity)
else:
    activity = "Go outdoors!"
    print("It is warm today.")
    print(activity)
 

raining = input("Is it raining today? (yes/no): ")
 
if raining == "yes":
    print("Do an indoor activity or Take an umbrella!")
 
homework_time = int(input("Enter homework time in minutes: "))
 
if homework_time > 60:
    needs_break = "yes"
    print("Your Homework is very long today.")
    print("Take a short break before you", activity)
else:
    needs_break = "no"
    print("Your Homework is short today.")
    print("No long break needed before you", activity)
 
free_time = input("Do you have free time today? (yes/no): ")
 
if free_time == "yes":
    final_task = "hobby time"
    print("You have free time today.")
    print("Enjoy your", final_task)
else:
    final_task = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", final_task)
 
print("")
print("Daily activity check complete!")
 
print("===== DAILY ACTIVITY PLANNER =====")
print("Temperature:", temperature)
print("Activity Chosen:", activity)
print("Raining:", raining)
print("Study Break Needed:", needs_break)
print("Final Task:", final_task)
print("==================================")
