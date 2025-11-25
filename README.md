# cptec-inpe

Este script percorre IDs de cidades do serviço XML do CPTEC/INPE e salva as cidades válidas em um arquivo `result.txt`.

## Como funciona

- Faz requisições para cada ID (1 a 5564).
- Lê o XML retornado.
- Extrai nome e UF da cidade.
- Salva no formato: `ID - Nome, UF`.

## 📚 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: Git e Python.

## 💾 Instalação

Siga as instruções abaixo:
```bash
  # Clone este repositório
  $ git clone https://github.com/gustavoalvim41/NOME_DO_PROJETO.git

  # Acesse a pasta do projeto no terminal/cmd
  $ cd cptec-inpe

  # Instale as dependências
  $ pip install -r requirements.txt

  # Certifique-se que o Python está corretamente instalado em sua máquina
  # Execute este comando no terminal/cmd para iniciar o projeto
  $ python main.py
```
