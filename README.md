# Proyecto de Resumen de Transacciones

Este proyecto es una función de AWS Lambda que lee datos de transacciones de un archivo CSV en Amazon S3, procesa los datos y envía un resumen de las transacciones por correo electrónico.

## Requisitos

- Docker
- Python 3.8 o superior
- Acceso a AWS S3
- Configuración de las credenciales de AWS para el entorno de ejecución

## Configuración

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Actualiza las siguientes variables en el archivo `lambda_function.py`:

   - `bucket_name`: Nombre del bucket de S3 donde se encuentra el archivo CSV.
   - `csv_file_name`: Nombre del archivo CSV que contiene los datos de las transacciones.
   - `sender`: Dirección de correo electrónico del remitente.
   - `recipients`: Lista de direcciones de correo electrónico de los destinatarios.

## Ejecución Local

1. Desde la línea de comandos, ejecuta el siguiente comando para probar la función Lambda localmente:

````
```
docker build -t lambda-resumen-transacciones .
```
````

2. Ejecuta el contenedor Docker con el siguiente comando:
````
```
docker run -p 9000:8080 lambda-resumen-transacciones
```
````

3. Abre otra terminal y envía una solicitud POST para probar la función Lambda localmente:
````
```
curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
````