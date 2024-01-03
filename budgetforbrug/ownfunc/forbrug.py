import pandas as pd

from .helper import is_number


omkkat_liste = [
    "Omk2",
    "Omk3",
    "Omk4a",
    "Omk4b",
    "Omk4c",
    "Omk5a",
    "Omk5b",
    "Omk6",
    "Omk7",
]


def create_df(file_path_name, omk):
    df = pd.read_excel(file_path_name, sheet_name=omk["sheet_name"])
    df.rename(
        columns={
            df.columns[omk["belob"]]: "Belob",
            df.columns[omk["bevid"]]: "BevId",
            df.columns[omk["action"]]: "Action",
        },
        inplace=True,
    )
    return df


def bearbejd_ovr_df(df, partner, omkkat):
    df_num = df[df["Belob"].apply(is_number)]
    filt = df_num["Belob"] > 0
    df = df_num[filt][["BevId", "Action", "Belob"]]
    df["Partner"] = partner
    df["OmkostKat"] = omkkat
    return df


def bearbejd_omk1_df(df, partner, omkkat):
    df_gr_sum = df.groupby(["BevId", "Action"], as_index=False)["Belob"].sum()
    df_ialt = pd.DataFrame()
    df_ialt = pd.concat([df_ialt, df_gr_sum])
    df_ialt["Partner"] = partner
    df_ialt["OmkostKat"] = omkkat
    return df_ialt


def create_forbrug(file_name_finansielreport, partner, settings):
    df_ialt = pd.DataFrame()
    df = create_df(file_name_finansielreport, settings["Omk1"])
    df = bearbejd_omk1_df(df, partner, "Omk1")
    df_ialt = pd.concat([df_ialt, df], axis=0)
    for omkkat in omkkat_liste:
        df = create_df(file_name_finansielreport, settings[omkkat])
        df = bearbejd_ovr_df(df, partner, omkkat)
        df_ialt = pd.concat([df_ialt, df], axis=0)

    return df_ialt
