from flask import Flask
from api.eletronicos_api import eletronicos_bp
from api.estoque_api import estoque_bp
from api.produto_api import produto_bp
from api.recibo_api import recibo_bp
from api.relatorio_api import relatorio_bp
from api.vendas_api import vendas_bp
from api.vestuario_api import vestuario_bp

app = Flask(__name__)

# Registrando os Blueprints para cada API
app.register_blueprint(eletronicos_bp, url_prefix='/eletronicos')
app.register_blueprint(estoque_bp, url_prefix='/estoque')
app.register_blueprint(produto_bp, url_prefix='/produtos')
app.register_blueprint(recibo_bp, url_prefix='/recibos')
app.register_blueprint(relatorio_bp, url_prefix='/relatorios')
app.register_blueprint(vendas_bp, url_prefix='/vendas')
app.register_blueprint(vestuario_bp, url_prefix='/vestuario')

if __name__ == "__main__":
    app.run(debug=True)