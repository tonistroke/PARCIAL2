import pandas as pd
from pandas_datareader import wb

Immunization_measles = "SH.IMM.MEAS"
Immunization_DPT = "SH.IMM.IDPT"

Panama = ["PAN"]

wb.download(indicator = Immunization_measles, country = Panama, start = 2018, end = 2018)
