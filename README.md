# 🔢 Análisis Ingresos Públicos de Brasil 
Este proyecto realiza un análisis exploratorio de los ingresos recaudados por el gobierno de Brasil a lo largo de los años. El proceso comienza con una exploración y limpieza inicial de los datos, abordando problemas de tipos de datos, valores nulos y duplicados, seguido de la concatenación de los dataframes individuales para consolidar la información en un solo conjunto de datos, lo que permitió realizar un análisis exploratorio más completo empleando métricas de estadística descriptiva y continuando con la limpieza de datos.

El objetivo es en primer lugar ofrecer una visión general sobre los ingresos recaudados por el gobierno de Brasil y en segundo lugar,de forma más concreta, identificar en que áreas hay mayor problemática en la previsión de los ingresos (tanto de forma temporal, como más concretamente por entidades recaudadoras o partidas recaudadas). Para lograr estos resultados y conclusiones se emplean técnicas de agrupación y gráficos visuales que permiten identificar patrones, tendencias y áreas críticas que requieren de atención. 

## 📂 Estructura del Proyecto

        ├── datos       # Datos brutos de cada año
        ├── src       # Funciones soporte EDA 
        ├── .gitignore       # Ignora los archivos pkl de la carpeta datos
        ├── Eda_Inicial_Union.ipynb       # Primera exploración y limpieza de datos. Concatenación de los dataframes individuales 
        ├── Eda_Final.ipynb       # Exploración y limpieza del dataframe final
        ├── Analisis_Ingresos_Brasil.ipynb      # Principales resultados y conclusiones de los análisis
        ├── README.md       # Descripción del proyecto

## 💻 Instalación y Requisitos
Este proyecto utiliza:
- Python: Versión 3.13.0
- Jupyter Notebook (ejecutado a través de VSCode)
- Librerías principales: pandas, numpy, seaborn, matplotlib

## 📊 Resultados y Conclusiones

- **Principales Resultados de los Análisis**

    - Análisis de Ingresos Recaudados:
        - Entre 2013 y 2021 el gobierno de Brasil recaudó 25,6 billones de BRL. 
        - De Ingresos Corrientes e Ingresos de Capital proviene el 98,74% de la recaudación. 
        - Es el Ministerio de Economía el órgano que se ha llevado el 96,38% de la recaudación. 
        - En términos generales, la recaudación ha seguido un patrón ascendente, lo que indica un pronóstico positivo en el mediano y largo plazo.
    
    - Análisis Ingresos Previstos vs Recaudados:
        - Durante el mismo periodo, el gobierno de Brasil hizo una previsión en la recaudación de 28,3 billones de BRL. En la mayoría de los años, se observaron sobreestimaciones, excepto en 2020, donde las previsiones fueron las más precisas. 2017 destacó como el año con mayores discrepancias.
        - La Controladoria-geral da união fue la entidad con mayores dificultades en cumplir sus objetivos de recaudación, mostrando problemas persistentes tanto a nivel general como en unidades específicas, como la Diretoria de gestao interna (cgu).
        - En el análisis por categorías económicas, las Receitas de capital destacaron por sus problemas de previsión, especialmente en la fuente Alienação de bens, siendo el tipo Alienação de bens imóveis y su detalle Alien. bens imoveis de dom da uniao-dom diret, los más críticos en términos de desajustes entre previsión y recaudación.

Para obtener más detalle sobre tendencias, casos específicos, partidas económicas o incluso propuestas de mejora, consulte el informe completo de Analisis_Ingresos_Brasil

## 💡Próximos Pasos

Si hubiera dispuesto de más tiempo, profundizaría en las categorías de ingresos problemáticas: Realizar un análisis más detallado de las entidades y tipos de ingresos con peores desempeños, como Controladoria-geral da união y Alienação de bens imóveis, para identificar las causas subyacentes de sus bajos resultados y proponer soluciones efectivas. Este análisis permitiría obtener una visión más clara de las posibles mejoras a implementar y las estrategias para optimizar la recaudación en estas áreas.

## 🤝 Contribuciones
Agradezco cualquier contribución que pueda mejorar el proyecto. Si tienes alguna idea que aportar no dudes en contactar conmigo!
Algunos archivos no están incluidos en este repositorio debido a su tamaño. Si necesitas acceso a estos archivos para ejecutar el proyecto correctamente, por favor contáctame a través de LinkedIn o mi correo electrónico: raquelscv@gmail.com

## 👤 Autor 
**Raquel Sánchez** - https://github.com/raquelscv 