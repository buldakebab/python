import random


def getRandomFriend(number):
    if number ==1:
        return "Yeva"
    elif number == 2:
        return "Sia"
    elif number ==3:
        return "Emma"
    elif number ==4:
        return "Taira"

numb = random.randint(1,4)
friend =getRandomFriend(number= numb)

if friend =='Yeva':
    print("lightblue")
elif friend == "Sia":
    print('yellow')
elif friend == 'Emma':
    print("purple")
elif friend == "Taira":
    print("green")