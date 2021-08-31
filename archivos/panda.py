import pandas as pd

datos = pd.read_csv("c:/Users/iv886/Desktop/proyectos/saces/registro1.csv",sep=";",index_col=0,encoding="utf-8")

print(datos)