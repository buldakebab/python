# a= ["chips", "ice cream", "cereal", "ice coffee"]
# b=input ("ad new product")
# a.append ("cola")
# print (a)
# a.insert (1,"kebab")
# print (a)
# a. remove ("cereal")
# print(a)
# a.pop (1)
# print (a)
# for i in a:
#     print (i)





# a= []
# for i in range (1,101):
#     a.append (i) 
# print (a)
# for i in range (6):
#     a.insert (0,0)
# for i in range (10):
#     a.append (55)
# print (a)

# a.remove (55)
# print (a)

# for i in range (len(a)):

#     if 55 in a:
#         a.remove (55)
# print ("yeva")
# print (a)





# a= []
# for i in range (2,101, 2):
#     a.append (i)

# print (a)


# a= [27, 28, 97, 17, 87, 57,]
# b= 0
# for i in a:
#     if i <50:
#         b+=i
# print (b)



# a= [17, 38, 29, 30, 50, 85, 24, 16]
# b= 0
# for i in  a:
#     print (i)
#     if i >50:
#         b+=i 
# print (b)




# a= [17, 38, 29, 30, 50, 85, 24, 16]
# b= []
# for i in a:
#     if i <40:
#         b.append (i)
# print (b)
# print (a)


# a= [14, 59, 32, 12, 20, 31]
# b= 0
# for i in a:
#     if i >20:
#         b+=i
# print (b)



# a= [1, 2, 1, 1, 3, 2]
# b= []
# for i in a:
#     if i not in b:
#      b.append (i)
# print (b)
# print(list(set(a)))





# a= [17, 780, 90, 89, 89, 25, 190]
# b=a [1]
# for i in a:
#     if i > b:
#         b=i
# print (b)




 





# a = [17, 780, 90, 89, 89, 25, 190]

# print(min(a))

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044




# a= [18, -187, 2, 3, 4, 6, 8, 9, 20, 27, 59, 90,  -11, -12, -13, -14, -15]
# b=0
# c=0
# for i in a:
#     if i > 0:
#         b+=1
#     if i < 0:
#         c+=i
# print (c)
# print (b)
# [b, c]
# print ([b, c])






# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad



# a= [1, -2, 3, -4, 5]
# b= []
# for i in a:
#         b.append(i*-1)
# print (b)



# https://www.codewars.com/kata/515e271a311df0350d00000f




# a= [1, 4, 5]
# b= 0
# for i in a:
#     b+=i*i
# print (b)
















# a = ["pillow", "blenket", "flick", "ice", "flick", "cream"]
# b = []
# c = True 
# for i in a:
#     if i == "flick":
#         c = not c
#     b.append (c)
# print (b)









# a = ["keep", "remove", "keep", "remove", "keep", "remove"]
# b = []
# for i  in a:
#     if i  == "keep":
#         b.append (i)
# print (b)









a = ["Yeva", "Python", "Emma","School", "Sia","homework"]
b = []
for i in range (0,len(a),2):
    # if i % 2 == 0:
        b.append (a [i])
        print (i)
print (b)
