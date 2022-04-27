from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/second')
def second():
    return "This is second page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route("/success/<int:score>") #This was not in the task I added it.Ente 127.0.0.1:5000/success/90 to the address line (or any number)
def success (score):
    return "The person has passsed and the mark is "+ str(score)

@app.route("/fail/<int:score>")#This was not in the task I added it.Ente 127.0.0.1:5000/fail/25 to the address line
def fail (score):
    return "The person has failed and the mark is "+ str(score)

if __name__=="__main__":
    app.run(debug=False)