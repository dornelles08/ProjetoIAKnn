import csv
import requests

import json

arq = open('testes.csv', 'r')
dados = list(csv.reader(arq))
arq.close()

resultFinal = []

for dado in dados:
    labels = dado[-2:]
    infos = dado[:-2]

    response = requests.get(f"http://localhost:8000/polls/{','.join(infos)}")

    result = response.json()

    resultFinal.append({
        "labels": labels,
        "result": result,
        "same position": labels[0] == result['position'],
        "diff overall": float(result["overall"]) - float(labels[1])
    })


with open('json_data.json', 'w') as outfile:
    json.dump(resultFinal, outfile)
