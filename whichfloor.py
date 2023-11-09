maxStories = 80
userFloor = int(input("On what floor of the building is your office?"))

while userFloor > maxStories:
    print("Unfortunately, " , userFloor , "is not one of the " , maxStories , " floors of this building. Try again.")
    userFloor = int(input("On what floor of the building is your office?"))

print("Congrats! You work on floor: " , userFloor)