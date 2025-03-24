from datetime import datetime
import logging
from services.scrapping import scrap_pregao
from services.upload import upload_to_s3
from config import *
import os
import pandas as pd

def run():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app_pregao.log'),
            logging.StreamHandler()
        ]
    )


    logging.info('Iniciando o Script de Coleta de Dados do pregao da B3')
    logging.info('Iniciando o metodo de Raspagem dos dados do pregao da B3')
    logging.info('Endereco usado ' + URL )

    df = scrap_pregao(URL)

    while df.empty:
        logging.info('Ocorreu um Erro no processamento, nenhum dado foi raspado')
        df = scrap_pregao(URL)
    
    logging.info('Raspagem realizada com sucesso')

    df['Data'] = datetime.now().date()


    df["Data"] = pd.to_datetime(df["Data"], errors='coerce')
    df["Data"] = df["Data"].dt.strftime("%Y-%m-%d")
    df["Qtde. Teórica"] = df["Qtde. Teórica"].replace({r'\.': ''}, regex=True) 
    df["Qtde. Teórica"] = df["Qtde. Teórica"].astype(int)
    df["Part. (%)"] = df["Part. (%)"].replace({r'\,': '.'}, regex=True) 
    df["Part. (%)"] = df["Part. (%)"].astype(float)

    agora = datetime.now()
    data_hora_obj = agora.strftime("%Y%m%d")
    nome_arquivo = 'pregao-b3-' + data_hora_obj + '.parquet'
    caminho_arquivo = os.path.join('./files/', nome_arquivo)

    date = df["Data"].iloc[0]
    caminho_s3 = f"raw/Data={date}//{nome_arquivo}"

    df.to_parquet(caminho_arquivo, engine="pyarrow", index=False)

    logging.info('Arquivo '+ nome_arquivo + ' gerado com sucesso')
    logging.info('Subindo arquivo no AWS S3')

    retorno = upload_to_s3(caminho_arquivo, BUCKET_NAME, caminho_s3)
    logging.info(retorno)
    

run()


