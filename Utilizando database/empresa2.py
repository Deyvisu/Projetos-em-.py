import psycopg2

def criarTabelaDepartamentos(cur, conexao):

    cur.execute('''

    CREATE TABLE "Departamentos"(
    "DepartamentoID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "DepartamentoNome" varchar(255)

    );

    ''')

    conexao.commit()

def criarTabelaFuncionario2(cur, conexao):

    cur.execute('''

    CREATE TABLE "Funcionarios2"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255),
    "CPF" varchar(11),
    "Salário" money,
    "ID_departamento" int,
    CONSTRAINT fk_departamento 
        FOREIGN KEY ("ID_departamento") 
        REFERENCES "Departamentos"("DepartamentoID")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
    

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




try:

    con = psycopg2.connect(database="Empresa", user="postgres", password="postgres", host="localhost", port="5432")

    cursor = con.cursor()
    print("Conectado")

    inserirFuncionario(cursor, con)

    cursor.close()
    con.close()

except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)