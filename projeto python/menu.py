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
            atualizar_receita()
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

    print("\nReceita cadastrada!\n")
    
    
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
def atualizar_receita():
    nome_busca = input("\n\nDigite o nome da receita que deseja editar: ")
    receitas = []
    try:
        with open('receitas.txt', 'r') as arquivo:
            for linha in arquivo:
                receitas.append(linha.strip().split('|'))
    except FileNotFoundError:
        print("\nAinda não há receitas cadastradas.\n")
        return

    for i, receita in enumerate(receitas):
        if receita[0] == nome_busca:
            print("\nEscreva as novas informações ou deixe em branco se não desejar alterar: \n")
            nome = input("Nome da receita: ")
            pais_origem = input("País de origem da receita: ")
            ingredientes = input("Ingredientes da receita: ").split(',')
            modo_preparo = input("Modo de preparo da receita: ")

            # Verifica se foram fornecidos novos valores e os substitui, caso contrário, mantém os valores originais
            if nome.strip():
                receitas[i][0] = nome.strip()
            if pais_origem.strip():
                receitas[i][1] = pais_origem.strip()
            if ingredientes:
                receitas[i][2] = ','.join(ingredientes)
            if modo_preparo.strip():
                receitas[i][3] = modo_preparo.strip()

            with open('receitas.txt', 'w') as arquivo:
                for receita in receitas:
                    arquivo.write(f"{receita[0]}|{receita[1]}|{receita[2]}|{receita[3]}\n")

            print("\nReceita atualizada com sucesso!\n")
            return

    print("\nReceita não encontrada.\n")
    
# Função para deletar uma receita
def deletar():
    print("oi4")
    

        
        
if __name__ == "__main__":
    main()          