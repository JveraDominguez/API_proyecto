import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')

# Encuentra todas las tablas con la clase 'table-bordered'
tablas = soup.find_all('table', attrs={"class": "table-bordered"})

# Inicializa un DataFrame vacío
df = pd.DataFrame()

# Itera sobre las tablas
for i, tabla in enumerate(tablas, start=1):
    # Lee la tabla y convierte los datos en un DataFrame
    tabla_df = pd.read_html(str(tabla))[0]

    # Elimina la columna "Acciones" si existe
    if "Acciones" in tabla_df.columns:
        tabla_df = tabla_df.drop(columns=["Acciones"])

    # Concatena el DataFrame de la tabla al DataFrame principal
    df = pd.concat([df, tabla_df])

# Guarda el DataFrame en un archivo Excel
df.to_excel('Scrapingproyecto.xlsx', index=False)

print("Los datos se han guardado correctamente en 'output_pandas.xlsx'.")
