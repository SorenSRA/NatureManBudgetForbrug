import pandas as pd
import warnings


from os import listdir
from os.path import join

import ownfunc.forbrug as fbr
import ownfunc.budget as bgt

import ownfunc.helper as hlp
from ownfunc.partner_natman import Natureman


# Suppress UserWarning from openpyxl
warnings.filterwarnings("ignore", category=UserWarning)


def main():
    file_name_set = "./budgetforbrug/constants/data2.json"
    settings = hlp.indlaes_json(file_name_set)
    partner_info = Natureman()

    df_forbrug_ialt = pd.DataFrame()
    df_budget_ialt = pd.DataFrame()
    for partner, _ in partner_info.distspec.items():
        file_list = listdir(partner_info.get_file_path(partner))
        file_xlsx = [f for f in file_list if f[-4:].upper() == "XLSX"]
        df_forbrug_partner = fbr.create_forbrug(
            join(partner_info.get_file_path(partner), file_xlsx[0]), partner, settings
        )
        df_budget_partner = bgt.create_budget(
            join(partner_info.get_file_path(partner), file_xlsx[0]), partner, settings
        )

        df_forbrug_ialt = pd.concat([df_forbrug_ialt, df_forbrug_partner])
        df_budget_ialt = pd.concat([df_budget_ialt, df_budget_partner])

    return df_forbrug_ialt, df_budget_ialt


if __name__ == "__main__":
    df_forbrug, df_budget = main()
    file_name = "./Output/ForbrugBudget.xlsx"  # File name to save the Excel file
    with pd.ExcelWriter(file_name, mode="w") as writer:
        # Insert the DataFrame into an Excel sheet
        df_forbrug.to_excel(writer, sheet_name="Forbrug", index=False)
        df_budget.to_excel(writer, sheet_name="Budget", index=False)
