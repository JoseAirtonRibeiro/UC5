from classe_db import DBestoque
from datetime import datetime

class Compra:
    def __init__(self):
        self.entrada = DBestoque()
        self.listaHist = []


    def comprar_produtos(self,id_compra,cod,var,atributo,atributo2):
        comando_sql = f'insert into (quant) values ({var})'
        self.entrada.mycursor.execute(comando_sql)
        if int(cod) == id_compra:
            self.entrada.mycursor.execute(f'update Produtos inner join Compras_Produtos on '
                                          f'Produtos.cod = Compras_Produtos.cod_produtos '
                                          f'set Produtos.{atributo} = Produtos.{atributo} + Compras_Produtos.{atributo2}')
            self.entrada.conexao.commit()
        else:
            pass

