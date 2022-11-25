#tuple
# a=('asd','efg','ghj','rty','uio')
# print(a)
# print(a[1:4])
# s=('c','c++','java','python','sql,')# astersik(*)symbol used
# (f,c,*d)=s
# print(f)
# print(c)
# print(d)
# i=0
# while i<(len(s)):
#     print(s[i])
#     i=i+1 

# d=('fds','ghj','ijk','mno')
# for k in range(len(d)):
#     print(d[k])


# set
a={1,2,3,4}
b={'asd','qwe','fgh','zxc'}
print(a)
#a.update(b)
print(a)
a.discard(2)#remove the value in the exist not an error
print(a)
#a.remove(asd)#remove the vaue in the exit an error
c=a.issubset(b)
print(c)
c=a.issuperset(b)# is used in the a values in the common in the output is true 
print(c)
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
