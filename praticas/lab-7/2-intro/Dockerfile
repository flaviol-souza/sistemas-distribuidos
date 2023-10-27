# Herdar da imagem Python Docker
FROM python:3.7-slim

# Instale o pacote Flask via pip
RUN pip install flask==1.0.2

# Copie o código fonte para a pasta do aplicativo
COPY ./app.py /app/

#Muda o diretório de trabalho
WORKDIR /app/

# Defina "python" como ponto de entrada
ENTRYPOINT ["python"]

# Defina o comando como o nome do script
CMD ["app.py"]