from flask import Flask
from flask import render_template

app = Flask("Meine erste App")

#Einzelne Seite generieren, HTML verknüpfen
@app.route('/')
def hello_world():
    return render_template('index.html', name="Simon")


if __name__ == "__main__":
    app.run(debug=True, port=5000)


