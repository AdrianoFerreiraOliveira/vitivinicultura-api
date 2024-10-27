# Projeto API de Vitivinicultura

Este projeto implementa uma API para realizar scraping de dados do site da Embrapa, fornecendo informações sobre a produção, processamento, comercialização, importação e exportação de produtos vitivinícolas.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos](#requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Executando a API](#executando-a-api)
  - [Sem Docker](#sem-docker)
  - [Com Docker](#com-docker)
- [Autenticação JWT](#autenticação-jwt)
- [Documentação com Swagger](#documentação-com-swagger)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)

## Sobre o Projeto

Este projeto foi desenvolvido para coletar dados de vitivinicultura do site da Embrapa e disponibilizá-los através de uma API RESTful. A API é documentada utilizando o Swagger e possui autenticação JWT.

## Funcionalidades

- **Coleta de Dados**: Realiza scraping de dados do site da Embrapa.
- **Documentação**: Interface de documentação interativa usando Swagger.
- **Autenticação JWT**: Rotas protegidas para maior segurança.

## Tecnologias Utilizadas

- **Python** e **Flask**
- **JWT** para autenticação
- **Docker** para containerização (opcional)
- **Swagger** para documentação interativa

## Requisitos

- **Python 3.7** ou superior
- **Git**
- **Docker** (opcional)

## Instalação e Configuração

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/vitivinicultura-api.git
cd vitivinicultura-api
``` 

### Passo 2: Criar e Ativa um Ambiente Virtual
- python -m venv venv
- # No Windows
- venv\Scripts\activate
- No Linux/MacOS
- source venv/bin/activate

- ### Passo 3: Instalar Dependências
- pip install -r requirements.txt

## Executando a API
- docker build -t vitivinicultura-api .
- docker run -p 5000:5000 vitivinicultura-api
- python main.py

### Passo 3: Autenticação JWT
- A API utiliza autenticação JWT para proteger as rotas. Para obter um token, faça uma requisição POST para a rota /login com o seguinte Header:

```
{
  "username": "admin",
  "password": "senha123"
}
```
- Na resposta, você receberá um access token. Para acessar rotas protegidas, adicione o token no header Authorization:

{
  Authorization: Bearer seu_token_jwt 
}

### Documentação com Swagger
```
vitivinicultura-api/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── scraping.py
├── static/
│   └── swagger.json
├── venv/
├── .dockerignore
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

### Colocar seu token na área de Authorize

![image](https://github.com/user-attachments/assets/06b62551-9fb7-4689-bdc6-9383efec22d0)



### Arquitetura do Projeto

Descrição da Arquitetura do Projeto
- A arquitetura é dividida nas seguintes etapas:

- Ingestão de Dados: A API coleta dados do site da Embrapa por meio de scraping.
- API RESTful: Oferece endpoints para acesso aos dados de diferentes seções (produção, processamento, etc.). Implementa autenticação JWT para segurança.
- É possível armazenar temporariamente os dados no SQLITE por exemplo, no nosso caso não utilziamos ele para essa primeira etapa
- Recomendamos fortemente que utilizem o Docker pois temos inúmeros benefícios com ele
- Deploy na Render: A API é implantada na Render para garantir alta disponibilidade e escalabilidade.
- Consumo da API
- Tratamento de dados para o Modelo
- Modelo de Machine Learning (futuro): Um modelo que poderá ser treinado com os dados coletados e limpos.
- Ciclo de MLOPS para disponibilizar o modelo.
  
<img width="2043" alt="Diagrama Machine Learning Model" src="https://github.com/user-attachments/assets/0e9eeb03-2359-447d-a93a-53c0fd4d9e70">



### A Api se encontra dispónivel aqui:
https://vitivinicultura-api.onrender.com/swagger/

PS: Ressaltamos que o site da Embrapa pode sofrer de instabilidade ao testar a api, bem como serviços de terceiros utilizados com fins acadêmicos.




