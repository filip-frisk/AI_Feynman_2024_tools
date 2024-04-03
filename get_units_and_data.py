import pandas
import pickle
import os

FILEPATH_units = '../tools_AIF/FeynmanEquations.csv'

FOLDERPATH_data = '../tools_AIF/Feynman_with_units'

# read the csv file
df_units = pandas.read_csv(FILEPATH_units)

# create a hash table for the units with filename as key
units = {}
variable_columns = ['Formula','v1_name', 'v2_name', 'v3_name', 'v4_name', 'v5_name', 'v6_name', 'v7_name', 'v8_name', 'v9_name', 'v10_name','Output']
for index, row in df_units.iterrows():
    equations_list = []
    for column in variable_columns:
        if not pandas.isnull(row[column]):
            equations_list.append(row[column])
    units[row['Filename']] = equations_list


# delete nan value from dictionary
for key in list(units.keys()):
    if not units[key]:
        del units[key]

with open('units.pkl', 'wb') as f:
    pickle.dump(units, f)
