from bs4 import BeautifulSoup
from google import search
from collections import Counter
import urllib2, Date, Nameid

##bunch of methods needed for app.py

#this interprets the user-input question
def interpret(question):
    if (question.find("who")>-1) or (question.find("Who")>-1):
        return 0 #looking for a name
    elif (question.find("when")>-1) or (question.find("When")>-1):
        return 1 #looking for a date
    else:
        return -1 #invalid question, back to homepage

#extract links
#convert webpages to text with beautifulsoup
#run regexp on text
def getResults(inquiry, question_type):
    links = search(inquiry, stop=5)
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
                    results.append(date)
            else:
                for name in Nameid.run(soup.get_text()):
                    results.append(name)
        except urllib2.HTTPError, e:
            pass
    return results

#find mode of list

def getMode(results):
    data = Counter(results)
    return data.most_common(1)
