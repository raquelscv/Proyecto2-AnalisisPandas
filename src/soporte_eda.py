#funcion para obtener un dataframe que de informacion de los 5 valores unicos mas frecuentes (recuento y el % sobre el total) para una columna concreta
def info_valores_unicos(dataframe, columna):
    df_unicos = pd.DataFrame(dataframe[columna].value_counts().head())
    df_unicos["%/Total"] = round((dataframe[columna].value_counts().head())/(dataframe.shape[0])*100,2)
    return df_unicos

import pandas as pd 