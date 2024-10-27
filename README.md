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
