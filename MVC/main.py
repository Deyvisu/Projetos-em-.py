import psycopg2
from Controle.classeConexao import Conexão
from Modelo.classeFuncionario import *

try:
    con = Conexão("Empresa", "localHost", "5432", "postgres", "postgres")

    while True:

        listaFuncionarios = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        ORDER BY "ID" ASC
        ''')

        print("ID | Nome")
        for func in listaFuncionarios:
            print(f"{func[0]} - {func[1]} \n")

        funcionarioEscolhido = input("Escolha o ID do funcionário que deseja alterar: ")

        funcionarioConsulta = con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = '{funcionarioEscolhido}'
        ''')

        funcionario = Funcionario(funcionarioConsulta[0][0], funcionarioConsulta[0][1], funcionarioConsulta[0][2], funcionarioConsulta[0][3], funcionarioConsulta[0][4])

        print("O funcionário escolhido foi: ")
        print(funcionario.imprimirFuncionario())

        opcoes = "Você deseja alterar as informações básicas(1) ou o departamento(2)? "

        match opcoes:
            case "1":
                funcionario.nome = input("Digite o novo nome do funcionário: ")
                funcionario.cpf = input("Digite o novo cpf do funcionário: ")
                funcionario.salario = input("Digite o novo salário do funcionário: ")

                con.manipularBanco



    con._db.close()

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)