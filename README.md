# Election Analysis
Module 3 Challenge: Make use of Python language to open a CSV file contianing the data with the election results of three counties, calculate the total votes in the election, the total votes per county and per candidate and indicate the candidadte that has won the election.

## 1 Overview of Election Audit:

La comisión electoral del estado necesita analizar los resultados de las elecciones en 3 condados del estado, para ello hemos recibido un archivo CSV que contiene 3 columnas y 369,712 filas (incluyendo la fila con los encabezados de las columnas).

Los datos de las elecciones no contienen información acerca de votos en blanco o votos nulos.  **Cada línea del archivo CSV corresponde a un voto válido**.  Este dato es muy importante ya que el total de votos para cada candidato o County se obtiene contando la cantidad de líneas que cumplen una cierta condición.  

Al revisar los datos recibidos, encontramos lo siguiente:

La primera fila contiene los nombres de las columnas, que son los siguientes (de izquierda a derecha):

**Ballot ID**: En la primera columna se encuentran los números de serie de cada una de las boletas electorales.  El numero de serie es de 7 dígitos, todos son numéricos y ningún número de serie se repite o se encuentra duplicado.

**County**: En la segunda columna se encuentra el nombre del condado donde se usó la boleta electoral.  El nombre de cada condado es una cadena de texto de longitud variable y se repite en muchas líneas, dependiendo de la cantidad de votos emitidos en cada County.

**Candidate**: Los nombres de los candidatos se encuentran en la tercera columna.  También se trata de cadenas de texto de longitud variable y se repiten en muchas líneas, según la cantidad de votos obtenidos por cada Candidato.

A partir de esas tres columnas se puede obtener el resto de la información para dar los resultados de la elección, segun se describe en la próxima sección.





## 2 Election-Audit Results

## 3 Election Audit-Summary
