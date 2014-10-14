from bs4 import BeautifulSoup
from google import search
from collections import Counter
import urllib2, Date, Nameid

##bunch of methods needed for app.py

#this interprets the user-input question
def interpret(question):
    question = str(question)
    if ('who' in question) or ('Who' in question):
        return 0 #looking for a name
    elif ('when' in question) or ('When' in question):
        return 1 #looking for a date
    else:
        return -1 #invalid question, back to homepage

#extract links
#convert webpages to text with beautifulsoup
#run regexp on text
def getResults(inquiry, question_type):
    links = search(inquiry, lang='en', stop=10)
    results = []
    for url in links:
        req = urllib2.Request(url)
        try:
            webpage = urllib2.urlopen(req)
            webpagetext = webpage.read()
            webpage.close()
            soup = BeautifulSoup(webpagetext)
            if question_type == 1:
                for date in Date.findDates(soup.get_text()):
                    results.append(date.encode('ascii','ignore'))
            else:
                for name in Nameid.run(soup.get_text()):
                    results.append(name.encode('ascii','ignore'))
        except urllib2.HTTPError, e:
            pass
    return results

#find mode of list

#mode code taken from Christian Witts on stackoverflow
def getMode(results):
    data = Counter(results)
    return data.most_common(5)

#mode code taken from lxop on stackoverflow
#def getMode(results):
#    counts = {}
#    for item in results:
#        counts [item] = counts.get (item, 0) + 1
#    maxcount = 0
#    maxitem = None
#    for k, v in counts.items ():
#        if v > maxcount:
#            maxitem = k
#            maxcount = v
#    return maxitem
