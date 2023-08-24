import json
import numpy as np


dados = None

with open('json_data.json') as json_file:
    dados = json.load(json_file)

correctPosition = []
diffOverall = []

for dado in dados:
    labels = dado["labels"]
    result = dado["result"]

    correctPosition.append(labels[0] == result['position'])
    diffOverall.append(float(result["overall"]) - float(labels[1]))

diffOverall = np.array(diffOverall)
correctPosition = np.array(correctPosition)

unique, counts = np.unique(correctPosition, return_counts=True)

print(diffOverall.mean())
print(dict(zip(unique, counts)))