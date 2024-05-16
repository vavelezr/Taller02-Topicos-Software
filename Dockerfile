# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido actual del directorio al directorio de trabajo en la imagen
COPY . .


EXPOSE 8080
# Define el comando por defecto para ejecutar tu aplicación Flask
CMD ["python", "app.py"]
