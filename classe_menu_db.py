from classe_db import  DBestoque
from classe_compras import *
from classe_saida import *


class Menu:
    def __init__(self):
        DB = DBestoque()
        compra = Compra()
        saida = Saida()
        compra.entrada = DB
        saida.entrada2 = DB

        while True:
            entrada_fab = input('[1] - Cadastrar Fabricante\n[2] - Ja tenho um Fabricante\n[3] - Encerrar Programa\nN°:')
            if entrada_fab == '1':
                nome = input('Nome do Fabricante:')
                DB.cadastrar_fabri(nome)
            elif entrada_fab == '2':
                while entrada_fab == '2':
                    entrada2 = input('[1] - Cadastrar Produto\n[2] - Listar todos\n[3] - Alterar Produto\n[4] - Comprar do estoque \
                                    \n[5] - Saida do produto\n[6] - Listar todos os Fabricantes\n[0] - Sair\nN° ')
                    if entrada2 == '1':
                        cod = int(input('código do produto: '))
                        descricao = input('nome do produto: ')
                        codigo_fabri = input('codigo do Fabricante: ')
                        quantidade = input('quantidade: ')
                        DB.salvar_produtos(cod, descricao,codigo_fabri,quantidade)
                    elif entrada2 == '2':
                        DB.listar_produtos()
                    elif entrada2 == '3':
                        cod = int(input('código do produto:'))
                        valor = input('nova descricao: ')
                        chave = 'descricao'
                        DB.alterar_produtos(chave, valor, cod)
                    elif entrada2 == '4':
                        cod = int(input('código do produto:'))
                        var = int(input('quantidade comprada:'))
                        atributo = 'quantidade'
                        compra.comprar_produtos(cod,var,atributo)
                    elif entrada2 == '5':
                        cod = int(input('código do produto:'))
                        var = int(input('quantidade:'))
                        atributo = 'quantidade'
                        saida.sair_produtos(cod,var,atributo)
                    elif entrada2 == '6':
                        DB.listar_fabri()
                    elif entrada2 == '0':
                        print('Processo terminado')
                        break
                    else:
                        print('Invalido')
            elif entrada_fab == '3':
                print('...')
                break
            else:
                    print('Invalido')
