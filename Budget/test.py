import json

def umwandlung_budget():
    with open("budget.json") as open_file:
        json_als_dict = open_file.read()
        budget_dict = json.loads(json_als_dict)
        print(budget_dict)

umwandlung_budget()
