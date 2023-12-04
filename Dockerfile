# Imagen de python
FROM python:3.9

# Set del working directory
WORKDIR /usr/scr/app

# Copiamos los archivos al contenedor
COPY . .

# Comando para correr el programa
RUN pip install ibm-cos-sdk

CMD [ "python", "icos-demo-job.py" ] 