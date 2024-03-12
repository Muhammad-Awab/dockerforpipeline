# Pull de Imagen reducida
FROM python:3.11.1-slim

# Directorio de trabajo dentro del Docker
WORKDIR /app

EXPOSE 8080

# Copia el proyecto en el directorio definido
COPY . .





RUN pip3 install -r requirements.txt

# Comando por defecto que se ejecutará cuando se inicie el contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
