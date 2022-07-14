import mysql.connector as ms
import mysql.connector



class Func:
    def __init__(self):
        self.cone= mysql.connector.connect(host='localhost', user='root', password='q1w2e3', database='estoque')
        self.CRS = self.cone.cursor()



        def cadastra(self):
           descricao = ent_prod_desc['text']
           cod_fabri= input('DATA: ')
           
           
           self.cur.execute( "insert into Produtos "
                             "(descricao , cod_fabri) "
                             "value"
                            f"('{descricao}', '{datanas}')")
           self.conexao.commit()
            