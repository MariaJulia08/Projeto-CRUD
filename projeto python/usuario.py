import os
os.system('cls')

class user:                      #__ deixa a variável privada **(ver oq é __init__)**
    def __init__(self, nome, pais, ingredientes, preparo):
        self.__nome= nome
        self.__pais= pais
        self.__ingredientes= ingredientes
        self.__preparo= preparo
    
    def get_nome(self):
        return self.__nome
    
    def get_pais(self):
        return self.__pais
    
    def get_ingredientes(self):
        return self.__ingredientes
    
    def get_preparo(self):
        return self.__preparo
    
    def set_nome(self, nome):
        self.__nome= nome
        
    def set_pais(self, pais):
        self.__pais= pais
        
    def set_ingredientes(self, ingredientes):
        self.__ingredientes= ingredientes
        
    def set_preparo(self, preparo):
        self.__preparo= preparo
        
    def to_string(self):
        return (f"""{self.get_nome()}
{self.get_pais()}
{self.get_ingredientes()}
{self.get_preparo()}""")
        
usuario = user("Maria", "china", "ovos", "2horas")
print(usuario.to_string())