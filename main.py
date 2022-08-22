import pandas as pd
from pandas_datareader import wb
import mathplotlib.pyplot as plt


Immunization_measles = "SH.IMM.MEAS"
Immunization_DPT = "SH.IMM.IDPT"

Panama = ["PAN"]

df1 = wb.download(indicator = Immunization_measles, country = Panama, start = 1980, end = 2018)

df2 = wb.download(indicator = Immunization_DPT, country = Panama, start = 2010, end = 2018)

df = df1.merge(df2, on=country)

df.columns = ["año", "Porsentaje de niños (%)"]
df["Porsentaje de niños (%)"].plot(kind="bar")
