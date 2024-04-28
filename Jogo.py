import pickle

class JogoMedieval:
    def __init__(self):
        self.jogador = Jogador()
        self.bosses_derrotados = 0

    def iniciar(self):
        print("Bem-vindo ao Jogo Medieval!")
        self.exibir_menu()

    def exibir_menu(self):
        print("\nEscolha uma opção:")
        print("1. Explorar")
        print("2. Ver status do jogador")
        print("3. Salvar jogo")
        print("4. Sair")

        escolha = input(">> ")

        if escolha == "1":
            self.explorar()
        elif escolha == "2":
            self.jogador.exibir_status()
            self.exibir_menu()
        elif escolha == "3":
            self.salvar_jogo()
            self.exibir_menu()
        elif escolha == "4":
            print("Até logo!")
        else:
            print("Opção inválida.")
            self.exibir_menu()

    def explorar(self):
        print("Você está explorando...")
        encontrou_boss = random.choice([True, False])
        if encontrou_boss:
            self.encontrar_boss()
        else:
            encontrou_inimigo = random.choice([True, False])
            if encontrou_inimigo:
                self.combate()
            else:
                print("Você não encontrou nenhum inimigo desta vez.")
                self.exibir_menu()

    def encontrar_boss(self):
        # Código para encontrar Bosses...

    def combate(self):
        # Código de combate...

    def salvar_jogo(self):
        with open("savegame.dat", "wb") as save_file:
            pickle.dump(self, save_file)
        print("Progresso salvo com sucesso!")


# Restante do código continua igual...

# Criar uma instância do jogo e iniciar
jogo = JogoMedieval()
jogo.iniciar()