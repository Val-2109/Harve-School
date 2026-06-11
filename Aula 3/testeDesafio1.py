import pandas as pd
from datetime import datetime

df = pd.read_csv("/Aula 3/chamados.csv")
df["data_abertura"] = pd.to_datetime(df["data_abertura"])

