# Automação Linx Microvix + Interface CustomTkinter

Este projeto automatiza processos no sistema ERP Linx Microvix utilizando Selenium, com interface gráfica feita em `customtkinter`.

## Objetivo

- Automatizar tarefas repetitivas no sistema Microvix (ex: geração de relatórios)
- Oferecer uma interface simples para usuários executarem essas automações sem precisar programar

## Arquitetura do Projeto

O projeto segue o padrão de arquitetura em camadas (Layered):

- `main.py`: ponto de entrada da aplicação
- `interface/`: interface com o usuário via customtkinter
- `automacoes/`: scripts de automação com Selenium
- `controller/`: camada que faz a ponte entre interface e automação
- `utils/`: funções auxiliares
- `config.py`: configurações gerais

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt