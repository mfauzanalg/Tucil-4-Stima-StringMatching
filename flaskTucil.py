from flask import Flask, redirect, url_for, render_template, request
from BM import BM
from KMP import KMP
from ExtractInfo import process

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        pattern = request.form["key"]
        return redirect(url_for("result", patt=pattern))
    else:
        return render_template("index.html")

@app.route("/result/<patt>", methods =["POST", "GET"])
def result(patt):
    if request.method == "POST":
        pattern = request.form["key"]
        return redirect(url_for("result", patt=pattern))
    else:
        hasil = process("Corona Satu.txt", patt)
        hasil += process("Corona Dua.txt", patt)
        if not(hasil):
            return render_template("index.html", list=[["tidak ditemukan", "tidak ditemukan", "tidak ditemukan", "tidak ditemukan"]])
        else:
            return render_template("index.html", list=hasil)


if __name__ == "__main__":
    app.run()(debug=True)