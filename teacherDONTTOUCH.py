# import random


# def getRandomFriend(number):
#     if number ==1:
#         return "Yeva"
#     elif number == 2:
#         return "Sia"
#     elif number ==3:
#         return "Emma"
#     elif number ==4:
#         return "Taira"

# numb = random.randint(1,4)
# friend =getRandomFriend(number= numb)

# if friend =='Yeva':
#     print("lightblue")
# elif friend == "Sia":
#     print('yellow')
# elif friend == 'Emma':
#     print("purple")
# elif friend == "Taira":
#     print("green")



# def bar():
#     a=100
#     if a==1:
#         return 'yeva'
#     else:
#         return "Yeva likes coca cola"
#     print("Yeva likes kebab")
# bb=bar()
# print(bb)



# a=0
# def yeva():
#     global a
#     a=0
#     a+=1
#     print(a)
# for i in range(10):
#     yeva()

#pull request demonstration
def greeting(name):
    print("Hello", name)

def greetEmma():
    greeting("Emma")

def greetSia():
    greeting("Sia")

greetEmma()
greetSia()
a=lambda: greeting("Emma")
a()
