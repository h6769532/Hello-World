#coding:utf-8

import re

reload(__import__('sys')).setdefaultencoding('utf-8')

i = 0
while i<5: 
    #num = input("\nPlease input a number:")
    #num = int(num)+1
    i=i+1

#for(int i=0;i<5;i++)在python中写成以下形式
i = 0
for i in range(0,5):#range(0,5)返回值为数组{0,1,2,3,4}
    print(i)
    
    
def plus(a,b):
    return (a+b)

sum = plus(5,6)
print (str(sum))


li = [1, 2, 3]
length = len(li)
print(str(li[1]))

li.append(4)
for i in li:
    print(str(i))
    
tp = (1,2,3)
length = len(tp)
print(str(tp[2]))

dic1 = {}
dic1["first"] = 1
dic1["second"] = 2
dic1["third"] = 3
print("The thrid one is "+ str(dic1["third"]))    
dic1.pop("first")




dic2 = {"first" : 1,
        "second" : 2,
        "third" : 3}
print("The thrid one is "+ str(dic2["third"])) 

class Person(object):
    name = ""
    def __init__(self,name):
        self.name = name
    def resetName(self,name):
        self.name = name

p = Person("hjw")#调用__ini__
name = p.name
print(name)
p.resetName("sxr")
print(p.name)


def getCode(strn):
    #strn = strn.decode("utf-8")
    #pattern =  re.compile(r'\d+')
    output = re.sub("\D", "", strn) 
    return output

s= getCode("鲁北化工（600727）")
print(s)
