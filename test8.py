#file read 

# # try:
#     f=open("asd.txt","r")
#     #print(f.read())
#     #print(f.readline())# is used to the how many lies are read
#     #print(f.readline(3))#is used to the how many characters are print

#     print(f.readlines()) # is used to the al lines are singe line & convert the list type
# except:
#     print("file not found")
# else:
#     f.close()
# ooping in read method
# f=open("asd.txt","r")
# for i in f: # it has been the read all line in one by one
#     print(i)
# f.close()


# file write
#over write file
# f=open("asdf.txt","w")   # this is the  over write the file
# f.write("this is the python program")
# f.close()

# f=open("asdf.txt","r")
# print(f.read())

# append  write
f=open("asdf.txt","a")   # this is  append the file
f.write("\npython is an indentation")
f.close()
f=open("asdf.txt","r")
print(f.read())
f.close()

