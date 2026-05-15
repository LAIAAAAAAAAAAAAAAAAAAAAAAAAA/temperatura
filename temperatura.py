import random
import datetime
import csv
import os
import json

FILE_CSV = "temperatures.csv"
FILE_JSON = "temperatures.json"

def generar_temperatura():
    return round(random.uniform(10, 30), 2)

def guardar_dada():
    data = datetime.datetime.now()
    temperatura = generar_temperatura()
    existeix = os.path.isfile(FILE_CSV)

    with open(FILE_CSV, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not existeix:
            writer.writerow(["data", "temperatura"])
        writer.writerow([data.strftime("%Y-%m-%d %H:%M:%S"), temperatura])

    print(f"Dada guardada: {data} -> {temperatura}°C")

    dades = []
    with open(FILE_CSV, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dades.append({"data": row["data"], "temperatura": float(row["temperatura"])})

    with open(FILE_JSON, 'w') as f:
        json.dump(dades, f, indent=2)

    print("JSON actualitzat.")

guardar_dada()
