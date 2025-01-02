import pandas as pd

def info_valores_unicos(dataframe, columna):
    """
    Genera un resumen de los valores únicos más frecuentes en una columna de un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna para analizar los valores únicos.

    Returns:
        pd.DataFrame: Un DataFrame con los valores más frecuentes en la columna, 
                      incluyendo el porcentaje que representan respecto al total.
    """
    df_unicos = pd.DataFrame(dataframe[columna].value_counts().head())
    df_unicos["%/Total"] = round((dataframe[columna].value_counts().head())/(dataframe.shape[0])*100, 2)
    return df_unicos



def info_reporte(dataframe):
    """
    Genera un informe sobre los valores nulos y tipos de datos de un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame a analizar.

    Returns:
        pd.DataFrame: Un DataFrame con el número y porcentaje de valores nulos por columna,
                      junto con el tipo de dato de cada columna.
    """
    df_report = pd.DataFrame()
    df_report["Numero_nulos"] = dataframe.isnull().sum()
    df_report["Porcentaje_nulos"] = round((dataframe.isnull().sum()/dataframe.shape[0]*100), 2)
    df_report["Tipo_dato"] = dataframe.dtypes
    return df_report



def comprobacion_fechas(dataframe, columna):
    """
    Verifica si faltan fechas dentro del rango completo de fechas en una columna de un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna con valores de tipo fecha.

    Returns:
        pd.DatetimeIndex: Fechas que están ausentes en el rango completo de fechas.
    """
    fecha_completa = pd.date_range(start=dataframe[columna].min(), end=dataframe[columna].max())
    fechas_disponibles = dataframe[columna].unique()
    return fecha_completa.difference(fechas_disponibles)
