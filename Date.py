import re

test = "John Fitzgerald Kennedy, the 35th President of the United States, was assassinated at 12:30 p.m. Central Standard Time (18:30 UTC) on Friday, November 22, 1963, in Dealey Plaza, Dallas, Texas"
file = open("test.txt")
test = file.read()
file.close()
test.strip("'")

months =['January', 'February','March','April','May','June',
        'July','August','September','October','November','December'
        'Jan','Feb','Mar','Apr','May','June','July',
        'Aug','Sept','Oct',',Nov','Dec']

dates = []

text = "Sept 21, 2014 Hello October 8, 1994 Lala 21, 2012"


def findDates(s):
    dates = re.findall(r"[A-Za-z]+ [0-9]{1,2}, [0-9]{4}",s)
    dates = checkMonths(dates)
    print (dates)
    return dates
    
def checkMonths(listy):
    newlist = []
    for thing in listy:
        if thing.split()[0] in months:
            newlist.append(thing)
    return newlist
'''
def checkNum(listy):
    newlist = []
    for thing in listy:
        if thing.split()[1]#add stuff:
            newlist.append(thing)
    return newlist
'''
if __name__ == "__main__":
    findDates(text)
    findDates(test)
