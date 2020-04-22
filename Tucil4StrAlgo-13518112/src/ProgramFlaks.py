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
    else: # tergantung kepada input user
        hasil = process("../test/Corona Satu.txt", patt)
        hasil += process("../test/Corona Dua.txt", patt)
        hasil = process("../test/Corona Satu.txt", patt)
        hasil += process("../test/Corona Dua.txt", patt)
        hasil += process("../test/Corona Tiga.txt", patt)
        hasil += process("../test/Corona Empat.txt", patt)
        hasil += process("../test/Corona Lima.txt", patt)
        hasil += process("../test/Corona Enam.txt", patt)
        hasil += process("../test/Corona Tujuh.txt", patt)
        hasil += process("../test/Corona Delapan.txt", patt)
        hasil += process("../test/Corona Sembilan.txt", patt)
        hasil += process("../test/Corona Sepuluh.txt", patt)
        if not(hasil):
            return render_template("index.html", list=[["tidak ditemukan", "tidak ditemukan", "tidak ditemukan", "tidak ditemukan"]])
        else:
            return render_template("index.html", list=hasil)

@app.route("/perihal")
def perihal():
    return render_template("perihal.html")

if __name__ == "__main__":
    app.run()(debug=True)