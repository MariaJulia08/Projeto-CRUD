import os 
os.system("cls")

# Função para o menu principal
def main():
    while True:
        print("""\n\n
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝\n\n""")
        print("""             
1. Cadastrar Nova Receita
              
2. Visualizar Todas as Receita

3. Editar Receita

4. Excluir Receita

5. Adicionar Receita aos Favoritos

6. Visualizar Receitas Favoritas

7. Remover Receita dos Favoritos

8. Sugerir Receita Aleatória

9. Filtrar Receitas por País

10. Filtrar poringredientes alérgicos

11. Sair\n\n""")
        opcao = input("BEM VINDO RAFA, QUAL DAS OPÇÕES ACIMA VAI SER ESCOLHIDA?  ")
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            visualizar()
        elif opcao == '3':
            atualizar()
        elif opcao == '4':
            deletar()
        elif opcao == '5':
            adicionar_favorito()
        elif opcao == '6':
            visualizar_favoritos()
        elif opcao == '7':
            remover_favorito()
        elif opcao == '8':
            sugerir_receita_aleatoria()
        elif opcao == '9':
            filtrar_por_pais()
        elif opcao == '10':
            filtrar_por_ingrediente()
        elif opcao == '11':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")





# Função para cadastrar uma nova receita
def adicionar():
    nome = input("Digite o nome da receita: ")
    pais_origem = input("Digite o país de origem da receita: ")
    ingredientes = input("Digite os ingredientes da receita, separando-os com vírgula: ").split(',')
    modo_preparo = input("Digite o modo de preparo da receita: ")
    
    with open('receitas.txt', 'a') as arquivo:
        arquivo.write(f"{nome}|{pais_origem}|{','.join(ingredientes)}|{modo_preparo}\n")

    print("\nReceita cadastrada!\n")
    
    
# Função para visualizar todas as receitas cadastradas
def visualizar():
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
    buscar = input("\n\nDigite o nome da receita que deseja excluir: ")
    receitas = []
    try:
        with open('receitas.txt', 'r') as arquivo:
            receitas = arquivo.readlines()
    except FileNotFoundError:
        print("\nAinda não há nenhuma receita cadastrada.\n")
        return

    with open('receitas.txt', 'w') as arquivo:
        encontrou = False
        for linha in receitas:
            if linha.split('|')[0].strip() != buscar:
                arquivo.write(linha)
            else:
                encontrou = True

        if encontrou:
            print("\nReceita excluída com sucesso!\n")
        else:
            print("\nReceita não encontrada.\n")

# Função para adicionar uma receita como favorita
def adicionar_favorito():
    nome_receita = input("Digite o nome da receita que deseja adicionar como favorita: ")
    try:
        with open('receitas.txt', 'r') as arquivo:
            receitas = arquivo.readlines()
        with open('receitas.txt', 'w') as arquivo:
            for linha in receitas:
                if nome_receita in linha:
                    if '*' not in linha:
                        linha = linha.strip() + " *\n"
                arquivo.write(linha)
        print("Receita adicionada aos favoritos!\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

def remover_favorito():
    nome_receita = input("Digite o nome da receita que deseja remover dos favoritos: ")
    try:
        with open('receitas.txt', 'r') as arquivo:
            receitas = arquivo.readlines()
        with open('receitas.txt', 'w') as arquivo:
            for linha in receitas:
                if nome_receita in linha:
                    if '*' in linha:
                        linha = linha.replace('*', '')
                arquivo.write(linha)
        print("Receita removida dos favoritos!\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

def visualizar_favoritos():
    try:
        with open('receitas.txt', 'r') as arquivo:
            print("""\n\n
███████╗░█████╗░██╗░░░██╗░█████╗░██████╗░██╗████████╗░█████╗░░██████╗██╗
██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██╔════╝╚═╝
█████╗░░███████║╚██╗░██╔╝██║░░██║██████╔╝██║░░░██║░░░███████║╚█████╗░░░░
██╔══╝░░██╔══██║░╚████╔╝░██║░░██║██╔══██╗██║░░░██║░░░██╔══██║░╚═══██╗░░░
██║░░░░░██║░░██║░░╚██╔╝░░╚█████╔╝██║░░██║██║░░░██║░░░██║░░██║██████╔╝██╗
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝\n\n""")
            for linha in arquivo:
                if '*' in linha:
                    nome, pais_origem, ingredientes, modo_preparo = linha.strip().split('|')
                    print("\nNome:", nome.strip('')) 
                    print("País de Origem:", pais_origem)
                    print("Ingredientes:")
                    for ingrediente in ingredientes.split(','):
                        print("- ", ingrediente.strip()) 
                    print("Modo de Preparo:", modo_preparo)
                    print('-' * 50)  
    except FileNotFoundError:
        print("Ainda não há receitas favoritas.\n")

# Função para sugerir uma receita aleatória
import random
def sugerir_receita_aleatoria():
    try:
        with open('receitas.txt', 'r') as arquivo:
            receitas = arquivo.readlines()
        if receitas:
            receita_aleatoria = random.choice(receitas).strip().split('|')
            print("Receita Aleatória Sugerida:")
            print("\nNome:", receita_aleatoria[0])
            print("País de Origem:", receita_aleatoria[1])
            print("Ingredientes:")
            for ingrediente in receita_aleatoria[2].split(','):
                print("- ", ingrediente.strip())
            print("Modo de Preparo:", receita_aleatoria[3],"\n\n")
        else:
            print("Ainda não há receitas cadastradas.\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")
        
        
        
        
def filtrar_por_pais():
    pais = input("\n\nDigite o país de origem para filtrar as receitas: ")
    try:
        with open('receitas.txt', 'r') as arquivo:
            encontradas = False
            for linha in arquivo:
                nome, pais_origem, ingredientes, modo_preparo = linha.strip().split('|')
                if pais_origem.lower() == pais.lower():
                    print(f"\nNome: {nome}")
                    print(f"País de Origem: {pais_origem}")
                    print(f"Ingredientes: {', '.join(ingredientes.split(','))}")
                    print(f"Modo de Preparo: {modo_preparo}")
                    encontradas = True
            if not encontradas:
                print(f"\nNão foram encontradas receitas do país {pais}.\n")
    except FileNotFoundError:
        print("\nAinda não há receitas cadastradas.\n")   

#Função para procurar receitas por ingredientes e reportar ingredientes alérgicos
alergicos = ['amendoim', 'leite', 'trigo', 'castanha', 'camarão', 'lagosta','peixe','soja', "coco"]
def filtrar_por_ingrediente():
    ingrediente = input("Digite o ingrediente para procurar as receitas: ").lower()
    
    if ingrediente in alergicos: 
        print(f"\nAtenção: O ingrediente '{ingrediente}' pode causar alergia em algumas pessoas.\n")
    
    try:
        with open('receitas.txt', 'r') as arquivo:
            receitas = [linha.strip().split('|') for linha in arquivo]
            receitas_encontradas = [receita for receita in receitas if ingrediente in [ing.strip().lower() for ing in receita[2].split(',')]]
            
            if receitas_encontradas:
                print(f"\nA seguir estão as receitas que contêm o ingrediente '{ingrediente}':\n")
                for receita in receitas_encontradas:
                    print(f"\nNome: {receita[0]}")
                    print(f"País de Origem: {receita[1]}")
                    print(f"Ingredientes: {', '.join(receita[2].split(','))}")
                    print(f"Modo de Preparo: {receita[3]}")

                    ingredientes_receita = [ing.strip().lower() for ing in receita[2].split(',')]
                    ingredientes_alergicos = [ing for ing in ingredientes_receita if ing in alergicos]
                    
                    if ingredientes_alergicos:
                        print(f"\nAtenção! Esta receita contém ingredientes que podem causar alergia à algumas pessoas: {', '.join(ingredientes_alergicos)}")

            else:
                print(f"\nNão foram encontradas receitas com o ingrediente '{ingrediente}'.\n")

    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")   
    
    
if __name__ == "__main__":
    main()