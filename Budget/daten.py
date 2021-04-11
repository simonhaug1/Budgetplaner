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


# ------Listet mit die Ausgaben aus dem json als dict auf
def umwandlung_ausgaben():
    with open("ausgabe.json") as open_file:
        json_als_dict = open_file.read()
        ausgaben_dict = json.loads(json_als_dict)

    ausgaben_auflistung = {}

    for key, value in ausgaben_dict.items():
        ausgaben_auflistung[value[0]] = value[3]

    return ausgaben_auflistung

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


#------Gibt mir die Summe aller selbst definierten Budgets aus
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

#------Gibt mir die Summe der eingetragenen Ausgaben, sortiert nach Budgetkategorien aus
def summe_n_budget():
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
        # print("budegt\n", budget_zahlen )
        # print("stand\n",bud)

        for key, val in bud.items():
            if key in budget_zahlen:
                budget_zahlen[key] = [budget_zahlen[key], int(val)]

        return budget_zahlen


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
