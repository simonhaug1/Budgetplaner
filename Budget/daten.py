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

def speichern_m_Variables(datei, key, value1, value2, value3, value4):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = [value1, value2, value3, value4]


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

#------Gibt mir die Summe alle eingegeben Ausgaben aus
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


#------Gibt mir die Summe alle eingegeben Budgets aus
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

#------Gibt mir die Summe der einzelnen Budgetkategorien aus
def summe_n_budget():
    with open('ausgabe.json') as open_file:
        json_als_string = open_file.read()
        aus = json.loads(json_als_string)

    with open('budget.json') as open_file:
        json_als_string = open_file.read()
        bud = json.loads(json_als_string)

    kat = {}

    for kategorie in bud:
        ausgabe_p_kategorie = 0
        for key, value in aus.items():
            if value[1] == kategorie:

                ausgabe_p_kategorie += float(value[0])
                kat[kategorie] = ausgabe_p_kategorie
            else:
                pass

        return kat


def ausgabe_speichern(ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name):
    datei_name = "ausgabe.json"
    zeitpunkt = datetime.now()
    speichern_m_Variables(datei_name, zeitpunkt, ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name)
    return zeitpunkt, ausgabe_number, ausgabe_kategorie, ausgabe_date, ausgabe_name


def budget_laden():
    datei_name = "budget.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
