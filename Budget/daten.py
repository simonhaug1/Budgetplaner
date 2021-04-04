from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

def speichern_m_Varibles(datei, key, value1, value2, value3):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = [value1, value2, value3]


    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

def umwandlung_json(datei):
    with open(datei) as open_file:
        json_als_dict = open_file.read()
        mein_eingelesenes_dict = loads(json_als_dict)

def umwandlung_budget():
    with open("budget.json") as open_file:
        json_als_dict = open_file.read()
        budget_dict = json.loads(json_als_dict)
        return budget_dict

def budget_speichern(budget_name, budget_number):
    datei_name = "budget.json"
    speichern(datei_name, budget_name, budget_number)
    return budget_name, budget_number

def ausgaben_zusammenzaehlen():
    # datei_name = "ausgabe.json"
    # content = datei_name.read()
    # wjdata = json.loads(content)
    # return value1


    with open('ausgabe.json') as open_file:
        json_als_string = open_file.read()
        mein_dict = json.loads(json_als_string)

        count = []

        for i, j in mein_dict.items():
            count.append(j[0])
            count = list(map(float, count))

            summe = sum(count)
        return summe

def budget_zusammenzaehlen():
    with open('budget.json') as open_file:
        json_als_string = open_file.read()
        mein_dict = json.loads(json_als_string)

        count = []
        for i, j in mein_dict.items():
            count.append(j)
            count = list(map(float, count))

            summe_b = sum(count)
        return summe_b







def ausgabe_speichern(ausgabe_name, ausgabe_number, kategorie, ausgabe_date):
    datei_name = "ausgabe.json"
    speichern_m_Varibles(datei_name, ausgabe_name, ausgabe_number, kategorie, ausgabe_date)
    return ausgabe_name, ausgabe_number, kategorie, ausgabe_date


def budget_laden():
    datei_name = "budget.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
