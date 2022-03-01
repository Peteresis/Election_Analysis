# Election Analysis
Module 3 Challenge: Make use of Python language to open a CSV file contianing the data with the congressional election results of three counties, calculate the total votes in the election, the total votes per county and per candidate and indicate the candidadte that has won the election.

## 1) Overview of Election Audit:

La comisión electoral del estado necesita analizar los resultados de las elecciones en 3 condados del estado, para ello hemos recibido un archivo CSV que contiene 3 columnas y 369,712 filas (incluyendo la fila con los encabezados de las columnas).

Los datos de las elecciones no contienen información acerca de votos en blanco o votos nulos.  **Cada línea del archivo CSV corresponde a un voto válido**.  Este dato es muy importante ya que el total de votos para cada candidato o County se obtiene contando la cantidad de líneas que cumplen una cierta condición.  

Al revisar los datos recibidos, encontramos lo siguiente:

La primera fila contiene los nombres de las columnas, que son los siguientes (de izquierda a derecha):

**Ballot ID**: En la primera columna se encuentran los números de serie de cada una de las boletas electorales.  El numero de serie es de 7 dígitos, todos son numéricos y ningún número de serie se repite o se encuentra duplicado.

**County**: En la segunda columna se encuentra el nombre del condado donde se usó la boleta electoral.  El nombre de cada condado es una cadena de texto de longitud variable y se repite en muchas líneas, dependiendo de la cantidad de votos emitidos en cada County.

**Candidate**: Los nombres de los candidatos se encuentran en la tercera columna.  También se trata de cadenas de texto de longitud variable y se repiten en muchas líneas, según la cantidad de votos obtenidos por cada Candidato.

A partir de esas tres columnas se puede obtener el resto de la información para dar los resultados de la elección, segun se describe en la próxima sección.


The state election commission needs to analyze the results of the elections in 3 counties of the state, for this purpose we have received a CSV file containing 3 columns and 369,712 rows (including the row with the column headers).

The election data does not contain information about blank votes or invalid votes.  **Each line of the CSV file corresponds to one valid vote.  This information is very important since the total number of votes for each candidate or county is obtained by counting the number of lines that meet certain criteria.  

When reviewing the data received, we found the following:

The first row contains the column names, which are as follows (from left to right):

**Ballot ID**: The first column contains the serial numbers of each of the ballots.  The serial number is 7 digits long, all are numeric and no serial number is repeated or duplicated.

**County**: In the second column is the name of the county where the ballot was used.  The name of each county is a text string of variable length and is repeated on many lines, depending on the number of votes cast in each county.

**Candidate**: The names of the candidates are in the third column.  These are also text strings of variable length and are repeated in many lines, depending on the number of votes obtained by each Candidate.

From these three columns you can obtain the rest of the information to give the election results, as described in the next section.




### **Fig. 1: Sample of the data received**
![Sample of the Original Data Received](https://github.com/Peteresis/Election_Analysis/blob/985384a19c594494d89f71477fdba0e7eebf5ecc/Data%20Sample.png)

## 2) Election-Audit Results

## 3) Election Audit-Summary
