import os 
os.system("cls")

# Função para o menu principal
def main():
    while True:
        print("""             
1. Cadastrar Nova Receita
              
2. Visualizar Todas as Receita

3. Editar Receita

4. Adicionar Receita aos Favoritos

5. Visualizar Receitas Favoritas

6. Remover Receita dos Favoritos

7. Sugerir Receita Aleatória

8. Filtrar Receitas por País

9. Sair\n\n""")
        opcao = input("BEM VINDO RAFA, QUAL DAS OPÇÕES ACIMA VAI SER ESCOLHIDA?  ")
        if opcao == '1':
            adicionar_receita()
        elif opcao == '2':
            visualizar_receitas()
        elif opcao == '3':
            editar_receita()
        elif opcao == '4':
            adicionar_favorito()
        elif opcao == '5':
            visualizar_favoritos()
        elif opcao == '6':
            remover_favorito()
        elif opcao == '7':
            sugerir_receita_aleatoria()
        elif opcao == '8':
            filtrar_por_pais()
        elif opcao == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")





# Função para cadastrar uma nova receita
def adicionar_receita():
    nome = input("Digite o nome da receita: ")
    pais_origem = input("Digite o país de origem da receita: ")
    ingredientes = input("Digite os ingredientes da receita, separando-os com vírgula").split(',')
    modo_preparo = input("Digite o modo de preparo da receita: ")
    
    with open('receitas.txt', 'a') as arquivo:
        arquivo.write(f"{nome}|{pais_origem}|{','.join(ingredientes)}|{modo_preparo}\n")

    print("\nReceita cadastrada com sucesso!\n")
    
    
# Função para visualizar todas as receitas cadastradas
def visualizar_receitas():
    try:
        with open('receitas.txt', 'r') as arquivo:
            print("""\n\n
██████╗░███████╗░█████╗░███████╗██╗████████╗░█████╗░░██████╗██╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔══██╗██╔════╝╚═╝
██████╔╝█████╗░░██║░░╚═╝█████╗░░██║░░░██║░░░███████║╚█████╗░░░░
██╔══██╗██╔══╝░░██║░░██╗██╔══╝░░██║░░░██║░░░██╔══██║░╚═══██╗░░░
██║░░██║███████╗╚█████╔╝███████╗██║░░░██║░░░██║░░██║██████╔╝██╗
╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝\n\n""")
            for linha in arquivo:
                nome, pais_origem, ingredientes, modo_preparo = linha.strip().split('|')
                print(f"\nNome: {nome}")
                print(f"País de Origem: {pais_origem}")
                print(f"Ingredientes: {', '.join(ingredientes.split(','))}")
                print(f"Modo de Preparo: {modo_preparo}")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

# Função para atualizar uma receita
def atualizar():
    print("oi3")
    
# Função para deletar uma receita
def deletar():
    print("oi4")
    

        
        
if __name__ == "__main__":
    main()          