# for i in range(5,20,3):
#     print ("Yeva")
#     print(i)
# a=4
# for i in range (1, 11):
#     #print (i, "*", a, "=", i * a)
#     print(f"{i} * {a} = {i*a}")


# a=55
# for i in range (1, 11):
#     print (i, "kebab cost" ,i * a , "euros")

# a=0
# for  i in range (1, 101, 2):
#      a=a+i
#      print (a)

# a=0
# while True:
#     print (a)
#     a=a+1
#     if a > 100:
#         break 
# while True:
#     a = input ("type a name") 
#     if a == "stop":
#         print ("yeva")
#         break
#     print ("hello", a)

#     Організувати безперервне введення чисел з клавіатури, доки користувач не введе 0. Після
# введення нуля, показати на екран кількість чисел, які були введені, їх загальну суму та
# середню арифметичну.


a = 0
b= 0
while True: 
    number =int(input ("enter a number (0 to stop): "))

    if number == 0: 
        print (a)
        print (b)

        break
    else:
        b = b + 1
        a = a + number
print ("finish")