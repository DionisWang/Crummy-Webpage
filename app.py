from Flask import Flask, render_template, request, reader

app = Flask(__name__)

#homepage with search bar
@app.route("/", methods=["GET","POST"])
def home(question = None):
    if request.method == "GET":
        return render_template("home.html", question=None)
    else:
        search = request.form["question"]
        if question == None:
            return render_template("home.html", question = None)
        else:
            if reader.interpret(search) == -1:
                return render_template("home.html", question = "error")
            else:
                return render_template("", question = search)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1234)


    

    
