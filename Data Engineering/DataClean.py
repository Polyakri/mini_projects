import pandas as pd
import csv

data = pd.read_csv("data.csv")


column_name = 'weight (kg)'
data = data[data[column_name] >= 35]

column_name = 'height (cm)'
data = data[data[column_name] >= 110]

column_name= 'age'
data = data[data[column_name] >= 18]


sex_column = 'sex'
data[sex_column] = data[sex_column].str[0].str.upper()

for i in range (len(data)):
    data.iloc[i, 0] = i + 1


print(data)
print (len(data))

output_file = "modified_data.csv"
data.to_csv(output_file, index=False)
