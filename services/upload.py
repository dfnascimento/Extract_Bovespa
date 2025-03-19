import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file, bucket_name, s3_file):
    '''
    Faz o upload de um arquivo local para o bucket S3.
    
    Parâmetros:
    local_file (str): Caminho do arquivo local.
    bucket_name (str): Nome do bucket S3.
    s3_file (str): Nome do arquivo no bucket S3.
    
    Retorno:
    str: Mensagem de retorno do upload.
    '''
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket_name, s3_file)
        return f"Upload bem-sucedido: {s3_file}"
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except NoCredentialsError:
        return "Credenciais AWS não encontradas."


