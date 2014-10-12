#this interprets the user-input question
#will need to run regex on the question first

def interpret(question):
    if (question.find("who")>-1) or (question.find("Who")>-1):
        return 0 #looking for a name
    elif (question.find("when")>-1) or (question.find("When")>-1):
        return 1 #looking for a date
    else:
        return -1 #invalid question, back to homepage
