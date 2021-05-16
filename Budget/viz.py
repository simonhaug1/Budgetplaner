import plotly.express as px
import json
from plotly.offline import plot
import pandas as pd

def pie_chart_ausgaben():
    with open('ausgabe.json') as open_file:
        json_als_string = open_file.read()
        aus = json.loads(json_als_string)

    name = []
    wert = []

    for key, value in aus.items():
        name.append(value[1])
        wert.append(value[0])
    df = pd.DataFrame(list(zip(name, wert)), columns=['Kategoriename', 'Wert'])

    fig1 = px.pie(df, values="Wert", names='Kategoriename', title="Für mehr Informationen über die Grafik hovern")
    div_pie = plot(fig1, output_type="div")
    return div_pie


