#functions
#arbitary arguments (*)
"""
def cmp(*detail):
    #print(detail)
    for i in detail:
        print(detail)
cmp('fraction','analytics','cts','dell','microsoft')
"""
# keyword arguments function
"""
def add(value1,value2):
    print(value1,"is",value2)
add(25,25)
"""

# arbitary keyword arguments(**)
"""
def values(**name):
    print(name)
values(name1='subash',name2='sundar',name3='asd',name4='fgh')
"""
#defaut parameter
"""
def detail(name='asd',district="tirunelveli"):
    print(name,'district is',district)
detail('subash','thuthukudi')
detail('sundar')
detail()
"""
# passing a list argument in fun
"""
def detail(name):
    for i in name:
        print(i)
data=['subash','sundar','assd','gfh','wer']
detail(data)
"""
#arguments
def func(*detail_list):
    course=[]
    for i in detail_list:
        course.append(i)
        return course
object=func('sql','python','java','c')
print(object)
