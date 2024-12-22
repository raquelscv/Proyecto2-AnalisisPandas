#funcion para obtener un dataframe que de informacion de los 5 valores unicos mas frecuentes (recuento y el % sobre el total) para una columna concreta
def info_valores_unicos(dataframe, columna):
    df_unicos = pd.DataFrame(dataframe[columna].value_counts().head())
    df_unicos["%/Total"] = round((dataframe[columna].value_counts().head())/(dataframe.shape[0])*100,2)
    return df_unicos

import pandas as pd 


#se genera una funcion para obtener un reporte para cada dataframe por cada año que de la informacion del numero de nulos, del porcentaje de nulos y del tipo de dato (por cada columna)
def info_reporte(dataframe):
    df_report = pd.DataFrame()
    df_report["Numero_nulos"] = dataframe.isnull().sum()
    df_report["Porcentaje_nulos"] = round((dataframe.isnull().sum()/dataframe.shape[0]*100), 2)
    df_report["Tipo_dato"] = dataframe.dtypes
    return df_report


#se genera la funcion
def comprobacion_fechas(dataframe, columna):
    fecha_completa = pd.date_range(start=dataframe[columna].min(), end = dataframe[columna].max())
    fechas_disponibles = dataframe[columna].unique()
    return fecha_completa.difference(fechas_disponibles)