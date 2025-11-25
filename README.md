# Scraping CPTEC/INPE – Busca de Cidades Litorâneas

Este script realiza scraping na API XML do CPTEC/INPE para identificar **cidades litorâneas** que possuem dados de *ondas* disponíveis.  
O script percorre todos os IDs de cidades e salva apenas as que retornam informações válidas no endpoint de ondas.

## O que ele faz

- Percorre o intervalo completo de IDs do CPTEC (1 a 5564).
- Faz requisições para o endpoint:  
  `http://servicos.cptec.inpe.br/XML/cidade/<id>/dia/0/ondas.xml`
- Se a API retornar nome e UF válidos, considera a cidade como **litorânea**.
- Registra cada cidade encontrada no arquivo `result.txt`.

## 📚 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: Git e Python.

## 💾 Instalação

Siga as instruções abaixo:
```bash
  # Clone este repositório
  $ git clone https://github.com/gustavoalvim41/NOME_DO_PROJETO.git

  # Acesse a pasta do projeto no terminal/cmd
  $ cd scraping-cptec-inpe

  # Instale as dependências
  $ pip install -r requirements.txt

  # Certifique-se que o Python está corretamente instalado em sua máquina
  # Execute este comando no terminal/cmd para iniciar o projeto
  $ python main.py
```
