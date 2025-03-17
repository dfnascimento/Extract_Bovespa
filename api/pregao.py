import os
from flask import Blueprint
from flasgger.utils import swag_from
from services.scrapping import scrap_pregao
from auth.autenticacao import auth

pregao = Blueprint('pregao', __name__ )

base_path = os.path.dirname(__file__) 
parent_path = os.path.abspath(os.path.join(base_path, os.pardir))
file_path = os.path.join(parent_path, 'docs', 'pregao.yml')

@pregao.route('/', methods=['GET'])
@swag_from(file_path)
@auth.login_required
def get_pregao():

    df = scrap_pregao()
    #comment
    try:
        df = df.to_json(orient='records', force_ascii=False, indent=4)
        return df, 200

    except Exception as e:
        return df, 200

