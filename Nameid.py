import re, operator
name=[]
lastname=[]
temp=open("resources/lite.txt","r")
for i in temp.readlines():
    name+=[i.strip("\n").lower()]
temp.close()
temp=open("resources/lastnames.txt","r")
for i in temp.readlines():
    lastname+=[i.strip("\n").lower()]
temp.close()
def fullname(d):
    r= re.findall( "[A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),2)
def titles(d):
    r= re.findall( "[A-Z][a-z][a-z]?\. [A-Z][a-z]+", d)
    return namefilter(check(r),1)
def partname(d):
    r= re.findall("[A-Z][a-z]+", d)
    return namefilter(check(r),0)
def middlename(d):
    r= re.findall("[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),2)
def suffix(d):
    r= re.findall( "[A-Z][a-z]+\s[A-Z][a-z]+\sJr|Sr", d)
    return namefilter(check(r),0)
def allnames(z):
    result = {}
    a= fullname(z)
    b= titles(z)
    c= partname(z)
    d= middlename(z)
    e= suffix(z)
    if not(a == None):
        result.update(a)
    if not(b == None):
        result.update(b)
    if not(c == None):
        result.update(c)
    if not(d == None):
        result.update(d)
    if not(e == None):
        result.update(e)
    return result
def check(d):
    temp={}
    clone=False
    for i in d:
        if (len(temp)==0):
            temp[i]=1
        else:
            for a in temp.keys():
                if(i == a):
                    temp[a]+=1
                else:
                    temp[i]=1
    return temp
def namefilter(d,index):
    temp={}
    for i in d.keys():
        if(index==0 or index==1):
            if(i.split(" ")[index].lower() in name):
                temp[i]=d[i]
        elif(index==2):
            if(i.split(" ")[0].lower() in name and i.split(" ")[-1].lower() in lastname):
                temp[i]=d[i]
    return temp
temp=open("testb.txt","r")
r=temp.read()
temp.close()
def run(s):
    result=allnames(s)
    return sorted(result, key=result.get, reverse=True)
for i in run(r):
    print i
