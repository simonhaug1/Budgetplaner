from flask import Flask, request
from flask import render_template
from Funktionen.visualisierung import balkendiagram

app = Flask("Hello World")


@app.route('/demo/')
def hello_world():
    return render_template('index.html', name="Simon")


@app.route("/testvis")
def testvis():
    grafik_div = balkendiagram()
    return render_template("vis.html", name="Simon", Grafik=grafik_div)


@app.route("/")
def test():
    return "success"

"""
@app.route('/hello/')
@app.route('/hello/<name>')
def begruessung(name=False):
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"
"""

@app.route("/demo/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html")


@app.route('/liste')
def liste():
    seiten_titel = "Partygäste"
    gaeste_liste = ["Simon", "Nina", "Pascal"]
    return render_template("auflistung.html", titel=seiten_titel, partygaeste=gaeste_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
