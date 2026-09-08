import random
import time
time.sleep(30)
attemts = 3 
1
number = random. randint (1, 10)
totalpoints = 0
while True:
    guess = int(input("type your guess 1, (-)? 10 :"))
    print (number)
    if guess == number:
        print ("you win")
        number = random. randint (1, 10)
        if attemts == 3:
         totalpoints = totalpoints + 1000
        elif attemts == 2:
         totalpoints = totalpoints + 500
        elif attemts == 1:
           totalpoints = totalpoints + 100
        print ("you have",totalpoints,"points")
        attemts = 3
    else:
        print ("try again") 
        attemts = attemts-1
        if totalpoints > 700:
           hint = input ("do you want to buy a hint")
           if hint == "yes":
              totalpoints = totalpoints - 700
              print ("Your number is in ", number-random.randint(1,2),"-",number+random.randint(1,2))
    if attemts == 0:
        print ("you lose")
        break
    
    


# import random

# )
# print (a)a = random. randint (1, 20