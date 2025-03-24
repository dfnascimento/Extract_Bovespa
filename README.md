# Coleta de Dados do Pregão da B3

## Descrição
Este projeto realiza a raspagem de dados do pregão da B3, processa as informações e as salva em um arquivo Parquet. Em seguida, o arquivo é enviado para um bucket da AWS S3.

## Funcionalidades
- Raspagem de dados do pregão da B3 utilizando Selenium.
- Processamento dos dados extraídos e formatação adequada.
- Armazenamento dos dados em arquivo Parquet.
- Upload automático do arquivo para o AWS S3.
- Logs detalhados para monitoramento do processo.

## Estrutura do Projeto
```
/
|-- app.py                # Script principal
|-- services/
|   |-- scrapping.py      # Módulo de raspagem de dados
|   |-- upload.py         # Módulo de upload para o AWS S3
|-- config.py             # Arquivo de configuração
|-- files/                # Pasta para armazenar arquivos gerados
|-- requirements.txt      # Dependências do projeto
|-- README.md             # Documentação do projeto
```

## Dependências
Certifique-se de instalar as dependências antes de executar o projeto:
```bash
pip install -r requirements.txt
```

## Como Executar
1. Configure as variáveis necessárias no arquivo `config.py`, incluindo a URL do pregão da B3 e as credenciais do AWS S3.
2. Execute o script principal:
```bash
python app.py
```

## Configuração
O arquivo `config.py` deve conter as variáveis:
```python
URL = "URL_DO_PREGAO_B3"
BUCKET_NAME = "NOME_DO_BUCKET_S3"
```

## Logs
Os logs são gerados no arquivo `app_pregao.log` e também exibidos no console para monitoramento.

## Autor
Diego de Faria do Nascimento

