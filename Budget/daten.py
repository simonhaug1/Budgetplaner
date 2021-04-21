from datetime import datetime
from datetime import date
import json

# Allgemeine Speichern Funktion
def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

# Funktion zum Speichern meiner Ausgaben
def speichern_m_Variables(datei, key, value1, value2, value3, value4):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = [value1, value2, value3, value4]


    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

# Funktion die die Ausgabe ins json schreibt
def ausgabe_speichern(ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name):
    datei_name = "ausgabe.json"
    zeitpunkt = datetime.now()
    speichern_m_Variables(datei_name, zeitpunkt, ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name)
    return zeitpunkt, ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name


# Funktion zum Umwandeln der erfassten Budgetkatogrien aus der json-Datei in ein dict.
def umwandlung_budget():
    try:
        with open("budget.json") as open_file:
            json_als_dict = open_file.read()
            budget_dict = json.loads(json_als_dict)
            return budget_dict
    except FileNotFoundError:
        budget_dict = {"Keine Daten vorhanden": ""}
        return budget_dict


# Funktion zum Umwandeln der erfassten Ausgaben aus der json-Datei in ein dict.
def umwandlung_ausgaben():
    try:
        with open("ausgabe.json") as open_file:
            json_als_dict = open_file.read()
            ausgaben_dict = json.loads(json_als_dict)

        # ausgaben_auflistung = {}

        # for key, value in ausgaben_dict.items():
        #     ausgaben_auflistung[value[2]] = value[0]

        return ausgaben_dict
    except FileNotFoundError:
        ausgaben_dict = {" ": "Keine Daten vorhanden"}
        return ausgaben_dict


# Allgemeine Funktion zum speichern
def budget_speichern(budget_name, budget_number):
    datei_name = "budget.json"
    speichern(datei_name, budget_name, budget_number)
    return budget_name, budget_number


# Funktion die mir die Summe alle eingegeben Ausgaben ausgibt
def ausgaben_zusammenzaehlen():
    try:
        with open('ausgabe.json') as open_file:
            json_als_string = open_file.read()
            mein_dict = json.loads(json_als_string)

            count = []

            for i, j in mein_dict.items():
                count.append(j[0])
                count = list(map(float, count))

                summe = sum(count)
            return summe
    except FileNotFoundError:
        summe = 0
        return summe


# Funktion die mir die Summe aller selbst definierten Budgets ausgibt
def budget_zusammenzaehlen():
    try:
        with open('budget.json') as open_file:
            json_als_string = open_file.read()
            mein_dict = json.loads(json_als_string)

            count = []
            for i, j in mein_dict.items():
                count.append(j)
                count = list(map(float, count))

                summe_b = sum(count)
            return summe_b
    except FileNotFoundError:
        summe_b = 1
        return summe_b


# Funktion die mir die Summe der eingetragenen Ausgaben, sortiert nach Budgetkategorien ausgibt
def summe_n_budget():
    try:
        with open('ausgabe.json') as open_file:
            json_als_string = open_file.read()
            aus = json.loads(json_als_string)

        with open('budget.json') as open_file:
            json_als_string = open_file.read()
            bud = json.loads(json_als_string)

        kat = {}

        budget_max = []
        ausgaben_stand = []

        for kategorie in bud:
            ausgabe_p_kategorie = 0
            for key, value in aus.items():
                if value[1] == kategorie:

                    ausgabe_p_kategorie += float(value[0])
                    kat[kategorie] = ausgabe_p_kategorie
                else:
                    pass

            for i, j in kat.items():
                budget_max.append(i)
                ausgaben_stand.append(int(j))

            budget_zahlen = {}
            for i in range(len(budget_max)):
                budget_zahlen[budget_max[i]] = ausgaben_stand[i]


            for key, val in bud.items():
                if key in budget_zahlen:
                    budget_zahlen[key] = [budget_zahlen[key], int(val)]

        return budget_zahlen
    except FileNotFoundError:
        budget_zahlen = {"Keine Daten vorhanden": [1, 0]}
        return budget_zahlen


# Funktion um aktuelles Datum (Monat) auszugeben
def datum_anzeigen():
    today = date.today()
    datum = today.strftime("%B %Y")
    return datum
