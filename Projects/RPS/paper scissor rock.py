rounds = int(input("numder of rounds you wanna play :"))
counter = 0
listOfRounds = []
while counter < rounds:
    listOfRounds.append(1)
    counter += 1

for counter in listOfRounds:
    plyr1 = input("player1 :please choose one character:")
    plyr2 = input("player2 :please choose one character:")
    # maincounter: rounds
    counter1 = 0
    counter2 = 0
    if (plyr1 == "paper" or plyr1 == "rock" or plyr1 == "scissor") and (plyr2 == "paper" or plyr2 == "rock"or plyr2 == "scissor"):
        if (plyr1 == "scissor" and plyr2 == "paper") or (plyr1 == "paper" and plyr2 == "rock") or (plyr1 == "rock"and plyr2 == "scissor"):
            # print("player1 won :D")
            print("----------------")
            counter1 += 1
        elif (plyr2 == "scissor" and plyr1 == "paper") or (plyr2 == "paper" and plyr1 == "rock") or (plyr2 == "rock"and plyr1 == "scissor"):
            # print("player2 won :D")
            print("----------------")
            counter2 += 1
        else:
        #     print("no one won :(!")
            print("----------------")
    else:
        print("wrong index!!!")
        listOfRounds.append(1)
        print("----------------")
if counter1>counter2:
    print (f" player1 is:{counter1} \n player2 is:{counter2}")
    print("plyer1 is winner")
elif counter2>counter1:
    print (f" player1 is:{counter1} \n player2 is:{counter2}")
    print ("plyer2 is winner")
else:
    print (f" player1 is:{counter1} \n player2 is:{counter2}")
    print ("you both sucked!")
