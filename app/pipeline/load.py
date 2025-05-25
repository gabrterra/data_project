import pandas as pd
import os

"""
Receber dataframe e salvar como excel

args: 
dataframe (pd.DataFrame)
output_path (str)
file_name (str)
"""

def load_excel(dataframe: pd.DataFrame, output_path: str, file_name: str) -> str:

    if not os.path.exists(output_path):
        os.mkdirs(output_path)

    dataframe.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"