import re

dates = []
text = "Sept 21, 2014 Hello October 8, 1994"
def findDates(s):
    dates = re.findall(r"[A-Za-z]+ [0-9]{1,2}, [0-9]{4}",s)
    print dates
    return dates

def checkNum(listy):
    newlist = []
    for thing in listy:
        if thing.split()[1]#add stuff:
            newlist.append(thing)
    return newlist

if __name__ == "__main__":
    findDates(text)
