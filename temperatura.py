import random
import datetime
import csv
import os

FILE = "temperatures.csv"

def generar_temperatura():
    return round(random.uniform(10, 30), 2)

def guardar_dada():
    data = datetime.datetime.now()
    temperatura = generar_temperatura()

    existeix = os.path.isfile(FILE)

    with open(FILE, mode='a', newline='') as f:
        writer = csv.writer(f)

        if not existeix:
            writer.writerow(["data", "temperatura"])

        writer.writerow([data.strftime("%Y-%m-%d %H:%M:%S"), temperatura])

    print(f"Dada guardada: {data} -> {temperatura}°C")

guardar_dada()
