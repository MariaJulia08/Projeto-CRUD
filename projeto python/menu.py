import os 
os.system("cls")

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

def checagem_opcao(opcao):
    if opcao.isnumeric():
        if int(opcao) < 1 or int(opcao) > 6:        
           return True
    elif opcao.isalpha():
             return True   

def check_menu():
    checagem_valor = menu()
    while checagem_opcao(checagem_valor): 
        print("Valor Inválido")         
        checagem_valor= menu()
    return int(checagem_valor)  

def adicionar():
    print("oi1")
    
def vizualizar():
    print("oi2")
    
def atualizar():
    print("oi3")
    
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