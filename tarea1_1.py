import pandas as pd
import matplotlib.pyplot as plt

archivo = r"avocado (1).csv"
df = pd.read_csv(archivo, sep=';')

def graficar_precio_por_region(df):
    regiones = ['Albany', 'Boston', 'Chicago']

    plt.figure(figsize=(10, 6))

    for region in regiones:
        df_region = df[df['region'] == region]
        plt.scatter(df_region['year'], df_region['AveragePrice'], label=region)

    plt.title('Precio Promedio del Aguacate por Año en 3 Regiones')
    plt.xlabel('Año')
    plt.ylabel('Precio Promedio')
    plt.legend()
    plt.grid(True)
    plt.show()