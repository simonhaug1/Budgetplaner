from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from datetime import datetime

import daten

app = Flask("templates")

# Erstellt mir die Startseite "Dashboard", wo ich die Übersicht über meine Ausgaben erhalten
@app.route("/")
def index():

    return render_template("index.html",  summe=daten.ausgaben_zusammenzaehlen(), budget_zahlen=daten.summe_n_budget(), summe_b=daten.budget_zusammenzaehlen(), kat=daten.summe_n_budget(), datum=daten.datum_anzeigen())


# Erstellt mir die Unterseite "Ausgabe hinzufügen", wo ich neue Ausgaben erfassen kann
@app.route("/add-ausgabe/", methods=['GET', 'POST'])
def ausgabe_hinzufügen(zeitpunkt=None):#Was macht ZEitpunkt=None??????
    if request.method == 'POST':
        ausgabe_name = request.form['ausgabe_name']
        ausgabe_number = request.form['ausgabe_number']
        ausgabe_kategorie = request.form['ausgabe_kategorie']
        ausgabe_date = request.form['ausgabe_date']
        ausgabe = daten.ausgabe_speichern(ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name)
        return redirect('/')


    return render_template("add_ausgabe.html", budget_dict=daten.umwandlung_budget())


# Erstellt mir die Unterseite "Budget hinzufügen", wo ich neue Budgetkategorien hinzufügen kann
@app.route("/add-budget/", methods=['GET', 'POST'])
def budget_hinzufügen():
    if request.method == 'POST':
        budget_name = request.form['budget_name']
        budget_number = request.form['budget_number']
        budget = daten.budget_speichern(budget_name, budget_number)
        return redirect('/budget/')


    return render_template("add_budget.html")


# Erstellt mir die Unterseite "Budget", wo ich eine Auflistung aller meiner erfassten Budgetkategorie habe
@app.route("/budget/")
def auflisten():

    return render_template("budget.html", budget_dict=daten.umwandlung_budget())


# Erstellt mir die Unterseite "Ausgaben", wo ich eine Auflistung aller meiner erfassten Ausgaben habe
@app.route("/ausgaben/")
def ausgaben_auflisten():

    return render_template("ausgaben.html", ausgaben_dict=daten.umwandlung_ausgaben())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
