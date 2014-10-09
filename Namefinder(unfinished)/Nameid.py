import re
name=[]
def dictionary(filename):
    temp=open("resources/"+filename,"r")
    global name
    for i in temp.readlines():
        name+=[i.strip("\n")]
    temp.close()
fname="None"
def fullname(d):
    r= re.findall( "[A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),0)
def titles(d):
    r= re.findall( "[A-Z][a-z][a-z]?\. [A-Z][a-z]+", d)
    return namefilter(check(r),1)
def partname(d):
    r= re.findall("[A-Z][a-z]*", d)
    return namefilter(check(r),0)
def middlename(d):
    r= re.findall("[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+", d)
    return namefilter(check(r),0)
def suffix(d):
    r= re.findall( "[A-Z][a-z]+\s[A-Z][a-z]+\sJr|Sr", d)
    return namefilter(check(r),0)
def allnames(d):
    return fullname(d)+titles(d)+partname(d)+middlename(d)+suffix(d)
def check(d):
    temp={}
    clone=False
    for i in d:
        for a in temp:
            if(i == a):
                clone=True
                temp[a]=temp[a]+1
        if(not clone):
            temp[i]=1
        clone=False
    return temp
def namefilter(d,index):
    temp=[]
    for i in d:
        for a in name:
            if(i.split(" ")[index].lower()==(a.lower())):
                temp+=[i]
                break
    return temp
#    def names(d,filename):
#    r=namefilter(fullname(d))+titles(d)
#    f=open((filename+"(result).txt"),"w")
#    for i in r:
#        print(i)
#        f.write(i+"\n")
#    f.close()
def run(s):
    return allnames(s)
for a in run("Dionis Wang. Jason. Ahasdhfl"):
    print a
