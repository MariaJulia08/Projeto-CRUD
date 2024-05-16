import os 
os.system("cls")

# Função para o menu principal
def menu():
    print("""\n\n█▀▄▀█ █▀▀ █▄░█ █░█ \n█░▀░█ ██▄ █░▀█ █▄█\n\n\n█▀█ █▀█ █ █▄░█ █▀▀ █ █▀█ ▄▀█ █░░\n█▀▀ █▀▄ █ █░▀█ █▄▄ █ █▀▀ █▀█ █▄▄\n\n
OPÇÕES:
[1]: ADICIONAR
[2]: VISUALIZAR
[3]: DELETAR
[4]: ATUALIZAR
[5]: FAVORITOS
[6]: SUGERIR RECEITA ALEATÓRIA
[7]: EXTRA 
[8]: SALVAR
 \n\n""")
    return input("escolha a opção desejada: ")

# Função para checar opção
def checagem_opcao(opcao):
    if opcao.isnumeric():
        if int(opcao) < 1 or int(opcao) > 6:        
           return True
    elif opcao.isalpha():
             return True   

# Função para checar valor
def check_menu():
    checagem_valor = menu()
    while checagem_opcao(checagem_valor): 
        print("Valor Inválido")         
        checagem_valor= menu()
    return int(checagem_valor)  

# Função para imprimir uma linha decorativa
def print_linha_embelezada():
    tamanho_terminal = 70
    linha = '-' * tamanho_terminal
    print(f"\n{linha}\n")

# Função para cadastrar uma nova receita
def adicionar():
    nome = input("Digite o nome da receita: ")
    pais_origem = input("Digite o país de origem da receita: ")
    ingredientes = input("Digite os ingredientes da receita (separados por vírgula): ").split(',')
    modo_preparo = input("Digite o modo de preparo da receita: ")
    
# Função para visualizar uma receita
def vizualizar():
    print("oi2")

# Função para atualizar uma receita
def atualizar():
    print("oi3")
    
# Função para deletar uma receita
def deletar():
    print("oi4")
    
def main(): 
    opcao = check_menu()
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        vizualizar()
    elif opcao == 3:
        deletar()
    elif opcao == 4:
        atualizar()
    elif opcao == 5:
        print("oi5")
    elif opcao == 6:
        print("Saindo...")
        
if __name__ == "__main__":
    main()          