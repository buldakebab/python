import random

plyar2_points = 0
plyar1_points = 0
while True:
    playar1 = input ("playar1 do you want to toss the cube")
    if playar1 == "yes":
        plyar1move = random. randint(1,6)
        print ("the cube rolled",plyar1move)
        plyar1_points = plyar1_points + plyar1move
        print ("playar1 is on",plyar1_points)

    if plyar1_points == 17:
        plyar1_points = 8
        print ("playar1 is on",plyar1_points)
    elif plyar1_points == 43:
        plyar1_points = 20
        print ("playar1 is on",plyar1_points)
    elif plyar1_points == 1:
        plyar1_points = 49
        print ("playar1 is on",plyar1_points)
    if plyar1_points > 49:
        print ("plyar1 wins")
        break
    playar2 = input ("playar2 do you want to toss the cube")
    if playar2 == "yes":
        plyar2move = random. randint(1,6)
        print ("the cube rolled",plyar2move)

    plyar2_points = plyar2_points + plyar2move
    print ("playar2 is on",plyar2_points)
    if  plyar2_points > 49:
       print  ("plyar2 wins")
       break
    if plyar2_points == 17:
         plyar2_points = 8
         print ("playar2 is on",plyar2_points)
    elif plyar2_points == 43:
         plyar2_points = 20
         print ("playar2 is on",plyar2_points)
    elif plyar2_points == 1:
         plyar2_points = 49
         print ("playar2 is on",plyar2_points)