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


def ausgabe_speichern(ausgabe_name, ausgabe_number):
    datei_name = "ausgabe.json"
    speichern(datei_name, ausgabe_name, ausgabe_number)
    return ausgabe_name, ausgabe_number

"""def budget_number_speichern(budget_number):
    datei_name = "budget.json"
    element_name = "number"
    speichern(datei_name, element_name, budget_number)
    return element_name, budget_number"""


def budget_laden():
    datei_name = "budget.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
