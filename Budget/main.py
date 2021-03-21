from flask import Flask
from flask import render_template
from flask import request
import daten

app = Flask("templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/budget/", methods=['GET', 'POST'])
def budget_hinzufügen():
    if request.method == 'POST':
        budget_name = request.form['budget_name']
        budget_number = request.form['budget_number']
        budget = daten.budget_speichern(budget_name, budget_number)
        rueckgabe_string = "budget gespeichert"
        return rueckgabe_string

    return render_template("base.html")


"""
@app.route("/auflistung")
def auflisten():
    budget = daten.budget_laden()

    budget_liste = ""
    for key, value in budget.items():
        zeile = str(key) + ": " + value + "<br>"
        budget_liste += zeile

    return budget.json"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)
