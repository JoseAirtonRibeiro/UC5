import mysql.connector
from classe_produto import *
from classe_fabricante import  *


class DBestoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost',user='root', password='q1w2e3', database='estoque')
        self.CURSOR = self.conexao.cursor()

    def salvar_produtos(self, cod, descricao, codigo_fabri, quantidade):
        comando_sql = 'select codigo from Fabricantes'
        self.CURSOR.execute(comando_sql)
        lista = self.CURSOR.fetchall()
        for i in lista:
            if int(codigo_fabri) == i[0]:
                obj_produto = Produto(cod, descricao, codigo_fabri, quantidade)
                comando_sql2 = f'insert into Produtos (cod,descricao, quantidade, codigo_fabri) value ("{obj_produto.cod}",' \
                               f'"{obj_produto.descricao}","{obj_produto.quantidade}","{obj_produto.codigo_fabri}")'
                self.CURSOR.execute(comando_sql2)
                self.conexao.commit()
                print('Produto Salvo!')
            else:
                pass

    def listar_produtos(self):
        comando_sql = 'select Produtos.descricao,nome, Produtos.codigo_fabri from Fabricantes inner join Produtos on Fabricantes.codigo = Produtos.codigo_fabri'
        self.CURSOR.execute(comando_sql)
        lista = self.CURSOR.fetchall()
        for i in lista:
            print('Código:', i[0])
            print('Nome do Produto:', i[1])
            print('Quantidade:', i[2])
            print('Nome do Fabricante:', i[3])


    def alterar_produtos(self, atributo, valor,cod):
        comando_sql = f'update Produtos set {atributo} = "{valor}" where cod = {cod}'
        self.CURSOR.execute(comando_sql)
        self.conexao.commit()
        print('Alteração')


    def cadastrar_fabri(self, nome):
        obj_fabri = Fabricante(nome)
        comando_sql = f'insert into Fabricantes (nome) value ("{obj_fabri.nome}")'
        self.CURSOR.execute(comando_sql)
        self.conexao.commit()
        print('Fabricante Cadastrado')

    def listar_fabri(self):
        comando_sql = 'select * from Fabricantes'
        self.CURSOR.execute(comando_sql)
        lista = self.CURSOR.fetchall()
        for i in lista:
            print('Código:', i[0])
            print('Nome do Fabricante:', i[1])



    def consulta(self):
        comando_sql = 'select Produtos.cod, Produtos.descricao, Produtos.quantidade, Fabricantes.nome from Produtos ' \
                      'inner join Fabricantes on Produtos.codigo_fabri = Fabricantes.codigo;'
        self.CURSOR.execute(comando_sql)
        lista = self.CURSOR.fetchall()
        for i in lista:
            print(i)
