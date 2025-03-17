from flask import Flask
from flasgger import Swagger
from api.pregao import pregao

app = Flask(__name__)
app.register_blueprint(pregao, url_prefix='/pregao')
swagger = Swagger(app)


@app.route('/')
def home():
    return """
    <h1>Bem-vindo à API de dados do pregão da B3</h1>
    <p>Esta é a página inicial da API.</p>
    <ul>
        <li><a href="/apidocs">Documentação</a></li>
    </ul>
    """


if __name__ == '__main__':
    app.run(debug=True)
