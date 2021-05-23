import plotly.express as px
import json
from plotly.offline import plot
import pandas as pd

def pie_chart_ausgaben():
    try:
        with open('ausgabe.json') as open_file:
            json_als_string = open_file.read()
            aus = json.loads(json_als_string)

        name = []
        wert = []

        for key, value in aus.items():
            name.append(value[1])
            wert.append(value[0])
        df = pd.DataFrame(list(zip(name, wert)), columns=['Kategoriename', 'Wert'])

        fig1 = px.pie(df, values="Wert", names='Kategoriename', template="presentation")
        div_pie = plot(fig1, output_type="div")
        return div_pie

    except FileNotFoundError:
        pass


def barchart_ausgaben():
    try:
        with open('ausgabe.json') as open_file:
            json_als_string = open_file.read()
            aus = json.loads(json_als_string)

        zeilen = []
        spalten = ["Betrag", "Kategorie", "Zeitpunkt", "Bezeichnung"]

        for i, j in aus.items():
            zeilen.append(j)

        df = pd.DataFrame(zeilen, columns=spalten )
        df.Betrag = df.Betrag.astype("int")

        fig = px.bar(df, x="Zeitpunkt", y="Betrag", color="Kategorie",  hover_name="Bezeichnung", template="presentation")
        div_bar_ausgabe = plot(fig, output_type="div")
        return div_bar_ausgabe

    except FileNotFoundError:
        pass

def barchart_budget():
    try:
        with open('budget.json') as open_file:
            json_als_string = open_file.read()
            bud = json.loads(json_als_string)

        # print(bud)
        Kategorie = []
        Betrag = []

        for i, j in bud.items():
            Kategorie.append(i)
            Betrag.append(j)

        dict = {'Kategorie': Kategorie, 'Betrag': Betrag}
        df = pd.DataFrame(dict)

        print(df)

        df.Betrag = df.Betrag.astype("int")

        fig = px.bar(df, x="Kategorie", y="Betrag", color="Kategorie", hover_name="Betrag", template="presentation")
        div_bar_budget = plot(fig, output_type="div")
        return div_bar_budget

    except FileNotFoundError:
        pass