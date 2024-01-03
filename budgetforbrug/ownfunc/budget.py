# -*- coding: utf-8 -*-
import pandas as pd

# file_path_name = r"C:\Filkassen\PythonMm\VSCode_projects\NatureManBudgetForbrug\Data\NSTLIFENatureManFinancialReporting2023Q2.xlsx"
# bevilling_sheet = "BevillingTildeling"


def create_budget_df(file_path_name, omk):
    df = pd.read_excel(file_path_name, sheet_name=omk["sheet_name"])
    return df


def create_budget(file_name_finansielreport, partner, settings):
    df_budget_indlaes = create_budget_df(file_name_finansielreport, settings["Budget"])

    df_budget = pd.DataFrame()
    for key, column in settings["Budget"]["column_list"].items():
        df_temp = df_budget_indlaes[df_budget_indlaes[column] > 0][
            ["BevillingsID", "Action number", column]
        ]
        df_temp["Partner"] = partner
        df_temp["OmkostKat"] = key

        df_temp.rename(
            columns={
                column: "Belob",
                "BevillingsID": "BevId",
                "Action number": "Action",
            },
            inplace=True,
        )
        df_budget = pd.concat([df_budget, df_temp], axis=0)

    df_budget.reset_index(drop=True, inplace=True)
    return df_budget


"""    
    df = bearbejd_omk1_df(df, partner, "Omk1")
    df_ialt = pd.concat([df_ialt, df], axis=0)
    for omkkat in omkkat_liste:
        df = create_df(file_name_finansielreport, settings[omkkat])
        df = bearbejd_ovr_df(df, partner, omkkat)
        df_ialt = pd.concat([df_ialt, df], axis=0)

    return df_ialt
    

"""


column_list = {
    "Omk1": "1. Personnel",
    "Omk2": "2. Travel and subsistence",
    "Omk3": "3. External assistance",
    "Omk4a": "4.a Infrastructure",
    "Omk4b": "4.b Equipment",
    "Omk4c": "4.c Prototype",
    "Omk5a": "5. Purchase or lease of land",
    "Omk6": "6. Consumables",
    "Omk7": "7. Other costs",
}
