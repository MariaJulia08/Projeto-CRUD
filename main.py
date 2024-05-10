import os
os.system('cls')

def menu():
    print("""Olá Rafael, escolha uma opção:\n
          1 - Adicionar receita
          2 - Vizualizar receita
          3 - Atualizar receita
          4 - Deletar receita\n""")
    return input("Digite a opção escolhida: ")   #digita as opções
    
    
def checagem_opcao(opcao):
    if opcao.isnumeric():
        if int(opcao) < 1 or int(opcao) > 4:        #retorna so as opções entre o intervalo e verifica se são letras ou números
           return True
    elif opcao.isalpha():
             return True   
    
def check_menu():
    checagem_valor = menu()
    while checagem_opcao(checagem_valor): 
        print("Valor Inválido")         #gera loop até escolher valor válido
        checagem_valor= menu()
    return int(checagem_valor)  #retorna um numero inteiro
    
def main(): 
    check_menu() 
    
if __name__ == "__main__":
    main()          #executa o arquivo principal 