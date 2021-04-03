from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect

import daten

app = Flask("templates")


@app.route("/")
def index():

    return render_template("index.html",  summe=daten.ausgaben_zusammenzaehlen())


@app.route("/add-ausgabe/", methods=['GET', 'POST'])
def ausgabe_hinzufügen():
    if request.method == 'POST':
        ausgabe_name = request.form['ausgabe_name']
        ausgabe_number = request.form['ausgabe_number']
        ausgabe_kategorie = request.form['kategorie']
        ausgabe_date = request.form['ausgabe_date']
        ausgabe = daten.ausgabe_speichern(ausgabe_name, ausgabe_number, ausgabe_kategorie, ausgabe_date)
        return redirect('/')


    return render_template("add_ausgabe.html", budget_dict=daten.umwandlung_budget())

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

    return render_template("budget.html", budget_dict=daten.umwandlung_budget())



if __name__ == "__main__":
    app.run(debug=True, port=5000)
