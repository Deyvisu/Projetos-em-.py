from PySimpleGUI import PySimpleGUI as sg

#para criar o layout, primeiro definimos o uso da biblioteca seguido da função
# 'theme' e entre parenteses, o nome do tema
# (pesquisar mais sobre os temas do PySimpleGUI)

sg.theme('Reddit')

#depois, definir o layout, com os parâmetros utilizando as classes da propria biblioteca
#sg.text('Usuário') para exibir o campo de usuário
#sg.input(key='usuário') para receber e ler o usuário
#sg.text('Senha') para exibir o campo de senha
#sg.input(key='senha') para receber e ler a senha
#logo em seguida utilizar  password_char='*' para que sua senha não seja exibida
#sg.checkbox('Salvar o login?') cria uma check box com a opção desejada
#sg.button('Entrar') Exibe o botão de entrar.
def telaCadastroLogin():
    layout = [
        [sg.Button('Realizar cadastro do usuário')],
        [sg.Button('Realizar login do usuário')],
        [sg.Button('Sair')]
    ]
    return sg.Window('U.F.A.', layout= layout, finalize=True)                                        #sg.Window = função da biblioteca que faz com que apareça na barra o nome do programa, seguido do layout(definida anteriormente)

def telaCadastro():
    layout = [
        [sg.Text('Usuário:'), sg.Input(key='usuário', size=(32,1))],
        [sg.Text('Senha:  '), sg.Input(key='senha',size=(32,1))],
        [sg.Text('Email:   '), sg.Input(key='email',size=(32,1))],
        [sg.Text('Confirme sua senha:  '), sg.Input(key='confirmacao',size=(21,1))],
        [sg.Button('Cadastrar')], [sg.Button('Voltar')]
    ]
    return sg.Window('Tela de cadastro', layout= layout, finalize=True)

def telaLogin():
    layout = [
        [sg.Text('Usuário:'), sg.Input(key='usuário', size=(30,0))],
        [sg.Text('Senha:  '), sg.Input(key='senha', password_char='*', size=(30,0)),],
        [sg.Checkbox('Lembrar login?')],
        [sg.Button('Entrar')], [sg.Button('Voltar')]
    ]
    return sg.Window('Tela de login', layout= layout, finalize=True)


janela1, janela2, janela3 = telaCadastroLogin(), None, None

while True:                                                                                      #vai manter a tela do programa aberta


    janela, eventos, valores = sg.read_all_windows()                                                #função que lê os eventos e os valores que vão estar na janela
    if janela == janela1 and eventos == sg.WINDOW_CLOSED:                                                              #condição para fechar a janela do programa
        break

    if janela == janela1 and eventos == 'Realizar cadastro do usuário':
        janela1.hide()
        janela2 = telaCadastro()
        
    if janela == janela1 and eventos == 'Realizar login do usuário':
        janela1.hide
        janela3 = telaLogin()
    
    if janela == janela1 and eventos == 'Sair':
        break
        
    if janela == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    
    if janela == janela3 and eventos == 'Voltar':
        janela3.hide()
        janela1.un_hide()

    if eventos == 'Entrar':                                                                      #condição que faz a leitura dos campos "Usuário" e "Senha", para o login
        if valores['usuário'] == 'Jonathan' and valores['senha'] == '123456':                    #'se(if) o valor(nome) que está guardado em 'usuário' e o valor(senha) que está guardada em 'senha' forem os mesmos, então faça:
            sg.popup('Login efetuado com sucesso! Bem vindo!')