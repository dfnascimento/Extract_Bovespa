
from flask_httpauth import HTTPBasicAuth
from config import USERNAME,SECRET_KEY

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Verifica se o usuário e senha são válidos.
    :param username: Nome de usuário
    :param password: Senha
    :return: O nome de usuário caso seja válido, caso contrário, retorna None
    
    1. Checa se o nome de usuário e senha são válidos.
    2. Caso seja válido, retorna o nome de usuário.
    3. Caso seja inválido, retorna None.
    4. Este método é chamado automaticamente pelo Flask-HTTPAuth para verificar se o usuário está autenticado.
    5. Se o método retornar None, o Flask-HTTPAuth irá redirecionar o usuário para o login.
    6. Se o método retornar um nome de usuário, o Flask-HTTPAuth irá permitir que o usuário faça requests à API."""
    if username == USERNAME and password == SECRET_KEY:
        return username


