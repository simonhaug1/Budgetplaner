## Ausgangslage
Den Überblick darüber zu behalten wohin der hart erarbeitete Lohn fliesst ist nicht immer 
ganz einfach. Man stellt sich die Fragen:
> *Wohin geht denn mein ganzes Geld?*

`BudgetPlaner` soll dieses Problem lösen, indem man seine Ausgaben und das monatliche 
Budget bequem im Tool eingeben kann. Somit sieht man sofort, für was man wie viel 
Ausgegeben hat und entsprechend auch, ob man sich nun bei weitern Ausgaben zurückhalten muss, 
oder noch genügen freie Mittel hat. 

## Projektidee
Das Tool soll eine Übersicht über die bereits getätigten Ausgaben inkl. Status des 
jeweiligen Budgets besitzen. Ausserdem sollen die Budgets selbst hinzugefügt, 
und wieder gelöscht werden können.
Das hinzufügen (und bei Bedarf auch das löschen) der Ausgaben soll einfach und schnell erfolgen.

## Installation
Um `BudgetPlaner` starten zu können muss folgendes installiert werden:
- `Python 3.9`
- `Flask`
- `Jinja2`
- `Plotly`
- `Pandas`

Das Tool kann danach von jedem Gerät aus dem Netzwerk über die IP Adresse und Port 5000 aufgerufen werden. 

## Workflow
![Workflow](Budget/doku/diagram.png)

### Dateneingabe
Es sind für die Ausgaben und für die Festlegung der Budget-Kategorien Dateneingaben durch den Nutzer notwendig.
Die Eingabe erfolgt über ein Formular, der Inhalt wird in ein json-File gespeichert.

### Datenverarbeitung/Speicherung
Die Daten werden in json-Dateien gespeichert. Dabei wird zwischen zwei Dateien unterschieden. Es gibt die `budget.json` und die `ausgaben.json`

##### Budet
Das File `budget.json` enthält folgende Informationen:
- Name der Budget-Kategorie
- Budget (als Zahl)

##### Ausgaben
Das File `ausgaben.json` enthält folgende Informationen:
- Timestamp als Key
- Betrag der Ausgabe
- Budget-Kategorie
- Datum der Ausgabe
- Name der Ausgabe

### Datenausgabe
Die Eingegebenen Ausgaben bzw. Budget-Kategorien werden direkt 
nach dem Erfassen in der jeweiligen Registerkarte als Tabelle angezeigt (Tabelle für Ausgaben und Budget). 
Zusätzlich fliessen diese Daten in die insgesamt 4 Diagramme ein (3 Plotly Diagramme und 1 html). 
Nachfolgend als Beispiel die Tabelle der Ausgaben.
![Budget](Budget/doku/tabelle_ausgabe.jpg)

## Benutzeranleitung
Der Nutzer hat die möglichkeit eine neue Budget-Kateogire hinzuzufügen oder zu löschen, sowie eine Ausgabe hinzuzufügen oder zu löschen. 
Ausserdem kann er im Dashboard die Ausgaben je Monat anzeigen lassen. Wie das genau funktioneirt, wird nachfolgende beschrieben.
### Budget hinzufügen
Wenn man nach der Installation das erste mal auf die Seite geht (Startseite), sind noch keine Daten vorhanden, das Dashboard zeigt in diesem Fall keine Daten an.
Man kan nun entweder eine Ausgabe hinzufügen (wenn keine eigene Budgetkategorie erfasst wurde ist es standardmässig "Andere") oder  zuerst seine Budget-Kategorien hinzufügen.
Dazu wählt man im rechten Bildschirmbereich das Symbol `Budget hinzufügen` aus. Es öffnet sich ein Eingabeformular wo man 
die Bezeichnung und den Betrag angeben kann. Nach dem speichern wird man direkt auf die Seite `Budget` weitergeleitet, wo man die Tabelle
aller bisher hinzugefügten Budgets sieht, ausserdem sieht man ein Diagramm, wo man optisch erkennen kann wie gross die jeweiligen Budgets sind.
Beachte, dass wenn man zwei mal den gleichen Namen hinzufügt, es nicht zwei Einträge gibt, sondern dass es dann den ersten Eintrag überschreibt (kann dazu verwendet werden um den Betrag der Budgetkategorie im Nachhinein anzupassen). 
![Budget](Budget/doku/budget.jpg)

### Ausgabe hinzufügen
Eine neue Ausgabe kann von jeder Unterseite durch das Plussymbol im unteren rechten Bildschirmrand erfassen.
Es öffnet sich ein Eingabeformular wo man den Betrag, die vorher erfasste Budgetkategorie, das Datum sowie die Bezeichnung angeben kann.
Nach dem speichern wird man direkt auf die Seite `Ausgaben` weitergeleitet, wo man analog zur Seite `Budget` die Tabelle aller bisher hinzugefügten 
Ausgaben sieht, ausserdem sieht man ein Diagramm, wo man sieht wann und wie viel bereits Ausgegen wurde. Die Tablle ist nach Datum sortiert.
![ausgabe](Budget/doku/ausgaben.jpg)

### Übersicht über die Ausgaben verschaffen
Auf der Startseite befindet sich das Dashboard, wo man sich einen Überblick über alle getätigten Ausgaben machen kann. 
Durch Auswahl des gewünschten Monats kann die Ansicht verändert werden (Standardmässig wird der aktuelle Monat angezeigt). Somit kann man im
Diagram `Budgetübersicht` pro Monat einsehen, wie viel man bereits pro Budgetkategorie ausgegeben hat.
Das Kreisdiagramm `Gesamtübersicht` zeigt wie viel Prozent die einzelnen Kateogrien an den Gesamtausgaben ausmachen (diese Ansicht ändert sich nicht mit dem Wechsel des Monats).
Da es sich um ein plotly express Diagramm handelt, kann durch hovern Zusatzinformationen im Diagramm abgefragt werden, sowie eine Filterung durchgeführt werden.
![dashboard](Budget/doku/dashboard.jpg)

### Ausgabe oder Budget löschen
Hat man eine Ausgabe oder eine Budgetkategorie falsch erfasst, oder möchte die 
Kategorie ersetzten, hat man die Möglichkeit über das Löschen Symbol (Abfalleimer) den jeweiligen Eintrag zu entfernen.
Dazu navigiert man auf die jeweilige Registerkarte `Ausgaben` oder `Budget` unten im Menüband und wählte dann den zu löschenden Eintrag aus.