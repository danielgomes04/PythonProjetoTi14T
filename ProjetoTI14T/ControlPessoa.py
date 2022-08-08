from Pessoa import Pessoa

class ControlPessoa:
    def __init__(self):
        self.person = Pessoa() #instanciando a classe pessoa
        self.opcao = -1

    def menu(self):
        print("Escolha uma das opções abaixo\n\n"
              "1. Cadastrar\n\n"
              "2. Consultar\n\n"
              "0. Sair")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()#chamando o menu
            if self.opcao == 0:
                print("Obrigado.")

            elif self.opcao == 1:
                print("Informe o nome: ")
                nome = input()
                print("\nInforme o telefone:")
                telefone = input()
                print("\nInforme o enderço:")
                endereco = input()
                self.person.cadastrar(nome, telefone, endereco)

            elif self.opcao == 2:
                print(self.person.consultarTudo())

            else:
                print("Opção inválida")

