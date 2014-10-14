from bs4 import BeautifulSoup
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
    links = search('inquiry', stop=10)
    results = []
    for link in links:
        webpage = urllib2.urlopen(link)
        webpagetext = webpage.read()
        webpage.close()
        soup = BeautifulSoup(webpagetext)
        txt = soup.get_text()
        results = []
        if question_type == 1:
            results.append(Date.findDates(txt))
        else:
            results.append(Nameid.run(txt))
    return results
