from flask import Flask, render_template, request
from google import search
import reader

app = Flask(__name__)

#homepage with search bar
@app.route("/", methods=["GET","POST"])
def home(question = None, results = None):
    if request.method == "GET":
        return render_template("home.html", question=None, results = None)
    else:
        inquiry = request.form["question"]
        #if no question inputted, return to home page
        if question == None:
            return render_template("home.html", question = None, results = None)
        else:
            #if invalid question, return to homepage
            if reader.interpret(search) == -1:
                return render_template("home.html", question = "error", results = None)
            #else send valid question and results to results page
            else:
                links = search('inquiry', stop=10)
                return render_template("results.html", question = inquiry, results = links)

#main
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1234)


    

    
