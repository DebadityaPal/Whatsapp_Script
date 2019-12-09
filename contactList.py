import pandas as pd
from pandas import DataFrame

#Read the contacts CSV file to import names
csvpath = #CSV PATH
names = pd.read_csv(csvpath)

#Append all the names to the list format as required by whatsapp.py
a_list = []
a_list.append(names['Name'].values)

#Print the list
print(a_list)