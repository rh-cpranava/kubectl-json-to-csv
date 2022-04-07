from flatten_json import flatten
import json
import pandas as pd

with open('data.json') as json_file:
    data = json.load(json_file)
    dic_flattened = [flatten(d) for d in data]
df = pd.DataFrame(dic_flattened)
df.to_csv('data.csv')
