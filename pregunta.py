"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #
    with open('clusters_report.txt', mode = 'r') as x:
        text = x.readlines()

    fin = []
    w = []

    for fila in text[4:]:
        if re.match('^ +\d+ +', fila):
            lista = fila.split()
            w.append(int(lista[0]))
            w.append(int(lista[1]))
            w.append(float(lista[2].replace(',','.')))
            w.append(' '.join(lista[4:]))
        elif re.match('^ +\w', fila):
            palabras = fila.split()
            palabras = ' '.join(palabras)
            w[3] += ' ' + palabras

        elif re.match('^\n', fila) or re.match('^ +$', fila):
            w[3] = w[3].replace('.', '')
            fin.append(w)
            w = []

    df = pd.DataFrame (fin, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df

