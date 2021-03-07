from flask import Flask, request
from flask import render_template

app = Flask("Hello World")


@app.route('/demo/')
def hello_world():
    return render_template('index.html', name="Simon")


@app.route("/test")
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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
