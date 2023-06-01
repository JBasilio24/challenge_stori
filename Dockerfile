FROM public.ecr.aws/lambda/python:3.8

# Copia los archivos necesarios
COPY lambda_function.py /
COPY utils /utils

# Establece las variables de entorno
ENV AWS_ACCESS_KEY_ID=<tu_access_key_id>
ENV AWS_SECRET_ACCESS_KEY=<tu_secret_access_key>
ENV AWS_SESSION_TOKEN=<tu_session_token>

# Establece el comando de inicio
CMD ["lambda_function.lambda_handler"]
