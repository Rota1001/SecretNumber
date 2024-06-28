from flask import Flask, redirect, flash, render_template, request, jsonify
import random

app = Flask(__name__)

data = [""] * 25
colorList = [2] * 25


@app.route("/captain")
def captain():
    return render_template("captain.html")

@app.route("/guessing")
def guessing():
    return render_template("guessing.html")

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/newgame")
def newGame():
    return render_template("newgame.html")

def setColor():
    global colorList
    colorList = []
    for i in range(9):
        colorList.append(0)
    for i in range(8):
        colorList.append(1)
    colorList.append(3)
    while len(colorList) != 25:
        colorList.append(2)
    random.shuffle(colorList)

def setString():
    global data
    data = []
    for i in range(25):
        data.append(str(i))

@app.route("/createNewgame", methods = ["GET"])
def newgame():
    setColor()
    setString()
    return jsonify({})



@app.route("/data", methods = ["GET"])
def getData():
    global data
    global colorList
    print(colorList)
    return jsonify({"data": data, "colorList": colorList})

if __name__ == "__main__":
    app.run(debug=True)