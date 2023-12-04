# Imagen de python
FROM python:3.9

# Set del working directory
WORKDIR /usr/scr/app

# Copiamos los archivos al contenedor
COPY . .

# Comando para correr el programa
RUN python -m pip install -r requirements.txt

CMD [ "python", "icos-demo-job.py" ] 