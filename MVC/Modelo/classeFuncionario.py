class Funcionario:
    def __init__(self, id, nome, cpf, salario, idDept):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.idDept = idDept


    def imprimirFuncionario(self):

        print(f'''
        Informações do funcionário:

        ID - {self.id}
        Nome - {self.nome}
        CPF - {self.cpf}
        Salario - {self.salario}
        ID Departamento - {self.idDept}
        
        ''')

    def inserirFuncionario(self, tabela):
        codigoSql = f'''
        INSERT INTO {tabela}
        VALUES(default, '{self.nome})', '{self.cpf}', '{self.salario}', '{self.idDept}'
        '''
        return codigoSql

    def atualizarFuncionario(self, tabela):
        codigoSql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self.nome})', "CPF" = '{self.cpf}', "Salario" = '{self.salario}',
        WHERE "ID" = '{self.id}'
        '''
        return codigoSql

    def atualizarDepartamentoFuncionario(self, tabela):
        codigoSql = f'''
        UPDATE "{tabela}"
        SET "ID_departamento" = '{self.idDept})',
        WHERE "ID" = '{self.id}'
        '''
        return codigoSql