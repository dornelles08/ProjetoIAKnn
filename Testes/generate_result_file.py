import csv
import json
from time import time

import requests

inicio = time()

arq = open('testes.csv', 'r')
dados = list(csv.reader(arq))
arq.close()

resultFinal = []

for dado in dados:
    labels = dado[-2:]
    infos = dado[:-2]

    response = requests.get(
        f"http://localhost:8000/classifier?data={','.join(infos)}")

    result = response.json()

    resultFinal.append({
        "labels": labels,
        "result": result,
        "same position": labels[0] == result['position'],
        "diff overall": float(result["overall"]) - float(labels[1])
    })


with open('json_data.json', 'w') as outfile:
    json.dump(resultFinal, outfile)

fim = time()

print(fim-inicio)
