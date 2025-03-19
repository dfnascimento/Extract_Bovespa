from datetime import datetime
import logging
from services.scrapping import scrap_pregao
from services.upload import upload_to_s3
from config import *
import os


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

    if df.empty:
        logging.info('Ocorreu um Erro no processamento, nenhum dado foi raspado')
        return
    
    logging.info('Raspagem realizada com sucesso')

    caminho_s3 = f"s3://`{BUCKET_NAME}ket`/dados-b3/ano={datetime.now().year}/mes={datetime.now().month}/dia={datetime.now().day}/pregao.parquet"

    agora = datetime.now()
    data_hora_obj = agora.strftime("%Y%m%d")
    nome_arquivo = 'pregao-b3-' + data_hora_obj + '.parquet'
    caminho_arquivo = os.path.join('./files/', nome_arquivo)

    df.to_parquet(caminho_arquivo, engine="pyarrow", index=False)

    logging.info('Arquivo '+ nome_arquivo + ' gerado com sucesso')
    logging.info('Subindo arquivo no AWS S3')

    retorno = upload_to_s3(caminho_arquivo, BUCKET_NAME, caminho_s3)
    logging.info(retorno)
    

run()
