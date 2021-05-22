def mainProgram():
     #a while loop will run forever until it's deliberatley exited
    while True:
         dieType = input("how many sides should the die have?  ")
        numberOfRolls = input("how many times do you want to roll?   ")
        rollTotal = 0

        print("here are your rolls; {}".format(myRolls))
        print("Your roll total was: {}".format(sum(myRolls)))
        print("Your highest roll was: {}".format(max(myRolls)))
        print("Your lowest roll was:  {}".format(min(myRolls)))

if __name__ =="__main__":
    diceEngine()

