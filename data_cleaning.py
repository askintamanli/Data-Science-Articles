import pandas as pd
import numpy as np

data = {"Name" : ["Bradd" , np.nan , "Scarlet" , "Mike" , "Margot" , np.nan],
        "Age" : [58 , 45 , 37 , np.nan , 31 , np.nan],
        "profession" : [np.nan , "Actor" , "Engineer" , "Journalist" , np.nan , np.nan]}

df = pd.DataFrame(data)

result = df

result = df.drop("Name" , axis= 1 )

result = df.drop(2)

result = df.isnull()

result = df[df["Name"].notnull()]

result = df.isnull().sum()

result = df.isnull().sum().sum()

result = df.dropna()

result = df.dropna(axis=1)

result = df.dropna(how="all")

result = df.dropna(subset= ["Name","Age"])

result = df.fillna(value="NO INPUT")

print(result)

