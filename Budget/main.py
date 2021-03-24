from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect

import daten

app = Flask("templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add-budget/", methods=['GET', 'POST'])
def budget_hinzufügen():
    if request.method == 'POST':
        budget_name = request.form['budget_name']
        budget_number = request.form['budget_number']
        budget = daten.budget_speichern(budget_name, budget_number)
        return redirect('/budget/')


    return render_template("add_budget.html")



@app.route("/budget/")
def auflisten():
    budget = daten.budget_laden()

    budget_liste = "<h1>Budgetkategorien</h1><br><ul class='budgetliste'>"
    for key, value in budget.items():
        zeile = "<li><span class='bezeichnung'>" + key + ":</span><span class='betrag'> " + value + "</span></li>"
        budget_liste += zeile
    budget_liste += "</ul><a href='/add-budget/' class='add'>Neues Element hinzufügen</a>"

    #return render_template("budget.html")
    return budget_liste



if __name__ == "__main__":
    app.run(debug=True, port=5000)
