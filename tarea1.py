import pandas as pd
import tarea1_1
archivo = r"avocado (1).csv"
df = pd.read_csv(archivo, sep=';')
n = int(input("cual pregunta del cuestionario quieres? "))
if n == 1:
    print(df.info())#informacion del archivo
elif n == 2:
    print(df.head(20))#las primeras 20
elif n == 3: 
    print(df.tail(20))# las ultimas 20
elif n == 4:
     columnas = ["AveragePrice"]  #especificar cual era la columna
     print("valor minimo ", df[columnas].min())   
     print("valor maximo ", df[columnas].max())    
     print("valor promedio ", df[columnas].mean())                  
elif n == 5:
     tarea1_1.graficar_precio_por_region(df)
else:
    print("ponga bien lo que quieres ")
