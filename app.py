from flask import Flask, redirect, flash, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/data", methods = ["GET"])
def data():
    if request.method == "GET":
        data = []
        for i in range(25):
            data.append(str(i))
        colorList = []
        for i in range(25):
            colorList.append(random.randint(0, 3))
        return jsonify({"data": data, "colorList": colorList})

if __name__ == "__main__":
    app.run(debug=True)