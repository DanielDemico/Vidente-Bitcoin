from flask import Flask,render_template,redirect
from prever import gerar_previsao

app= Flask(__name__)
previsao = None
@app.route("/")
def home():
    global previsao
    
    imagem = "./static/imagens/previsao.png"
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():
    global previsao
    previsao = gerar_previsao()
    
    
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)