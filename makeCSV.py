import pandas as pd
import json

# Make the data.json into a CSV file
df=pd.read_json("Results/data.json")

df.to_csv("Results/data.csv")