from flask import *
import psycopg2
from Modelos.classeCliente import Cliente
from Modelos.classeEndereço import Endereço
from Controle.classeConexao import Conexao


app = Flask(__name__)

try:
    con = Conexao("MEIC", "localhost","5432","postgres","postgres")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro - ", error)



@app.route("/")
def home():
    return render_template('HomePage.html')

@app.route("/CadastroCliente", methods = ("GET", "POST"))
def cadastrarCli():
    if request.method == "POST":
        usuario = Cliente("default", request.form['nomeCompleto'],request.form['idade'],request.form['dataNascimento'],request.form['cpf'],request.form['telefone'],request.form['email'],request.form['senha'])
        con.manipularBanco(usuario.inserirCliente("Cadastro_Cliente"))

        return render_template('HomePage.html')

    else:
        return render_template('CadastroCliente.html')
    

@app.route("/LoginCliente", methods = ("GET", "POST"))
def loginCli():
    if request.method == "GET":
        usuario = Cliente(None, None, None, None, None, None, request.form['emailLogin'], request.form['senhalogin'])
        resultado = con.consultarBanco(usuario.listarCliente("Cadastro_Cliente"))
        if resultado == []:
            #exibir mensagem de que o usuario não existe ou não está cadastrado
            return render_template('LoginCliente.html')
    else:
        return render_template('ExibirPerfilCliente.html')

if __name__== "__main__":
    app.run(debug=True)