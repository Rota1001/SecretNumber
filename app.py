from flask import Flask, redirect, flash, render_template, request, jsonify
import random

app = Flask(__name__)

data = [""] * 25
colorList = [2] * 25
wordlists = []

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

def setString(diff):
    global data
    global wordlists
    data = []
    if diff == "easy":
        for i in range(25):
            while True:
                word = random.choice(wordlists[0])
                if len(word) > 14:
                    continue
                if word not in data:
                    data.append(word)
                    break
    if diff == "hard":
        for i in range(25):
            while True:
                word = random.choice(wordlists[1])
                if len(word) > 14:
                    continue
                if word not in data:
                    data.append(word)
                    break
    if diff == "asia":
        for i in range(25):
            while True:
                word = random.choice(wordlists[2])
                if len(word) > 14:
                    continue
                if word not in data:
                    data.append(word)
                    break
    for i in range(25):
        data.append(str(i))

@app.route("/createNewgame", methods = ["GET"])
def newgame():
    setColor()
    setString(request.args["difficulty"])
    return jsonify({})



@app.route("/data", methods = ["GET"])
def getData():
    global data
    global colorList
    print(colorList)
    return jsonify({"data": data, "colorList": colorList})

if __name__ == "__main__":
    with open("wordlist.txt", "rb") as f:
        tmp = f.read().decode()
        tmp = tmp.split("$")
        for i in tmp:
            wordlists.append(i.split())
    app.run(debug=True)
    