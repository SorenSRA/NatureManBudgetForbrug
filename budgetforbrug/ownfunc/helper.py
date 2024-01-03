import pandas as pd
import json


def indlaes_json(file_name):
    try:
        with open(file_name, "r") as json_file:
            data_dict = json.load(json_file)
            return data_dict
    except:
        print("Fejl ifm indlæsning af JSON-file")
        return 99


def is_number(val):
    try:
        pd.to_numeric(val)
        return True
    except (ValueError, TypeError):
        return False
