# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o restante dos arquivos para o container
COPY . .

# Comando para executar a aplicação
CMD ["python", "main.py"]
