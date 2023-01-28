"""Funcionarios

    Func_ID - serial
    Func_Nome - varchar(255)
    Func_CPF - varchar(11) NOT NULL
    Func_Salario - money
    PRIMARY KEY("Func_ID")


"""
#Para se conectar com o banco de dados, primeiro faremos a conexão com a biblioteca:

import psycopg2

#Agora faremos a conexão:

def criarTabelaFuncionario(cur, conexao):

    cur.execute('''
    CREATE TABLE "Funcionarios"(
    "ID" serial,
    "Nome" varchar(255),
    "CPF" varchar(11) NOT NULL,
    "Salário" money DEFAULT 0.00,
    PRIMARY KEY("ID")

    );
    
    ''')

    conexao.commit()

def inserirFuncionario(cur, conexao):

    Nome = input("Digite o nome do funcionário que deseja inserir: ")
    while True:

        CPF = input("Digite o CPF do funcionário que deseja inserir: ")
        if len(CPF) != 11:
            print("Tamanho inválido! o CPF necessita conter 11 digitos")
        else:
            break

    Salario = float(input("Digite o salário do seu funcionário: "))

    cur.execute(f'''
    INSERT INTO "Funcionarios"
    VALUES(default, '{Nome}', '{CPF}', {Salario});
    ''')

    print(f"Funcionário {Nome} adicionado ao banco de dados de funcionários")

    conexao.commit()

    cur.execute('''
    SELECT * FROM "Funcionarios"
    
    ''')

    print(cur.fetchall())

def atualizarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    
    ''')

    print(cur.fetchall())

    ID= int(input("Digite o ID do funcionário que deseja atualizar: "))
    novoNome= input("Digite o novo nome do funcionário: ")
    novoSalario= float(input("Digite o novo salário do funcionário: "))

    cur.execute(f''' 
    
    UPDATE "Funcionarios"
    SET "Nome" = '{novoNome}', "Salário" = {novoSalario}
    WHERE "ID" = {ID}
    
    ''')

    print("Funcionario atualizado!")

    conexao.commit()

def deletarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    
    ''')

    print(cur.fetchall())

    ID= int(input("Digite o ID do funcionário que deseja deletar: "))

    cur.execute(f'''
    SELECT * FROM "Funcionarios"
    WHERE "ID" = {ID}
    ''')

    func = cur.fetchall()

    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {ID}

    ''')

    print(f"Funcionário {func} deletado!")

    conexao.commit()

def listarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    ''')

    print(cur.fetchall())

while True:
    try:

        con = psycopg2.connect(database="Empresa", user="postgres", password="postgres", host="localhost", port="5432")

                #O segundo passo é fazer o cursor:

        cursor = con.cursor()
        print("Conectado")

        print('''
            1. Ver funcionarios
            2. Inserir funcionario
            3. Modificar funcionario
            4. Remover funcionario
            0. Sair
            ''')

        opcaoMenu = input("Escolha o que deseja fazer: ")
        match opcaoMenu:
            case "1":
                listarFuncionario(cursor, con)
            case "2":
                inserirFuncionario(cursor, con)
            case "3":
                atualizarFuncionario(cursor, con)
            case "4":
                deletarFuncionario(cursor, con)
            case "0":
                print("Você escolheu sair do app, até breve!")
                break
            case _:
                print("Você digitou algo inválido!")
        
        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)