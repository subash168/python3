# if operator
# n=int(input("enter a no:"))
# if n % 2 == 0:
#     print(n,"the even no is:")

#if else stmt
# n=int(input("enter a no:"))
# if n % 2 == 0:
#     print(n,"the even no is:")
# else:
#     print(n,"the odd no is")

# nested if stmt
# a = int(input("enter the no:"))
# b= int(input("enter the age:"))
# if a>b:
#     print("the value a is greater")
#     if a<b:
#         print("the value b is greater")
# else:
#     print("the value are equal")



# whille loop
# i=1
# while i<=25:
#     if i%2 == 0:
#         i=i+1
#         continue;
#     print(i)
#     i+=1

#while loop
# num1 = 17  
# num2 = -12  
# while num1 > 5 and num2 < -5 : 
#     num1 -= 2  
#     num2 += 3  
#     print( (num1, num2) )  

#for loop
# details = ['subash','sundar','arun']
# for a in details:
#     print(a)

# print("--------------")
# for x in range(5):
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))


#     print(a+b)


for i in range(65,69,1):
    for j in range(65,69,1):
        print(chr(j),end="")
    print("")
else:#this block has for loop has full executed then else is executed otherwise not execute
    print("loop competed")





