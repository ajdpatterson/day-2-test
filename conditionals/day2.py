# SET is_it_raining = INPUT "Is it raining?"
# IF is_it_raining = "yes"
#   THEN PRINT "You should take the car!"
# ELSE 
#   IF distance < 5
#       THEN PRINT "You should walk!"
#   ELSE 
#       THEN PRINT "You should take the bus!"
# END

distance = 3
is_it_raining = input("Is it raining? ")

if is_it_raining == "yes":
    print("You should take the car!")
elif distance < 5:
    print(f"You're only going {distance} miles. You should walk!")
else:
    print(f"You're travelling {distance} miles. You should take the bus!")