from classe_db import DBestoque


class Saida:
    def __init__(self):
        self.entrada2 = DBestoque()
        self.listaHistSaida = []


    def sair_produtos(self,cod,var,atributo):
        comando_sql = 'select cod from Produtos'
        self.entrada2.mycursor.execute(comando_sql)
        lista = self.entrada2.mycursor.fetchall()
        for i in lista:
            if int(cod) == i[0]:
                self.entrada2.mycursor.execute(f'update Produtos set {atributo} = {atributo} - {int(var)} where cod = {cod}')
                self.entrada2.conexao.commit()

    
    def imprimir_hist_saida(self):
        for i in range(len(self.listaHistSaida)):
            print(self.listaHistSaida[i])