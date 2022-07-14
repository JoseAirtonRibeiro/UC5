import posiciona
from tkinter import *
from estoque_db import *


#Back = Backend()

fundo ='#1A192E'
letra ='Calibri 15'

janela = Tk()
janela.geometry('900x506')
janela.resizable(False, False)
janela.title('Estoque')

janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg,janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))
janela.bind('<KeyRelease>')
# ==============================================================================================================
# frames de cada tela
frame_menu = Frame(janela)
frame_menu_escolha = Frame(janela)
frame_escolha_term = Frame(janela)
frame_lista_pro = Frame(janela)
frame_lista_fab = Frame(janela)
frame_altera = Frame(janela)
frame_deleta = Frame(janela)
frame_compra = Frame(janela)
frame_cadastro_prod = Frame(janela)
# ==============================================================================================================
# carrega os primeiros frames
frame_menu.pack()
frame_menu_escolha.pack()
# ==============================================================================================================
#images 
confirma = PhotoImage(file='Foto/confirma.png')
busca = PhotoImage(file='Foto/chama_bt.png')
cadastra = PhotoImage(file='Foto/cadastra_bt.png')
saia = PhotoImage(file='Foto/bt_saia.png')
lista = PhotoImage(file='Foto/bt_lista.png')
compranovo = PhotoImage(file='Foto/bt_compra.png')
dele = PhotoImage(file='Foto/bt_deleta.png')
altera = PhotoImage(file='Foto/bt_altera.png')
clicmg = PhotoImage(file='Foto/bt_cliente.png')
fabcmg = PhotoImage(file='Foto/bt_fabri.png')
voltacmg = PhotoImage(file='Foto/bt_back.png')
menu = PhotoImage(file='Foto/Menu.png')
menu_prod = PhotoImage(file='Foto/Menu_Produto.png')
cadastro = PhotoImage(file='Foto/Cadastro.png')
Comprar = PhotoImage(file='Foto/Comprar.png')
alte = PhotoImage(file='Foto/Alterar.png')
deleta = PhotoImage(file='Foto/Deletar.png')
menu_prod_list = PhotoImage(file='Foto/SE_Produto.png')
menu_fabr_list = PhotoImage(file='Foto/SE_Fabricante.png')
menu_lista = PhotoImage(file='Foto/Menu_Escolha.png')
#==================================================================================================
lb_cad= Label(frame_cadastro_prod, image=cadastro, border=0)
bt_volt1= Button(frame_cadastro_prod, image=voltacmg, border=0, command=lambda: [frame_menu.pack(), frame_cadastro_prod.forget()])
ent_prod_desc= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)
ent_prod_cod= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)
ent_prod_codfabri= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)
bt_cad1= Button(frame_cadastro_prod, image=cadastra, border=0)
bt_cad2= Button(frame_cadastro_prod, image=cadastra, border=0)


ent_prod_nome= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra )
ent_prod_codfabri2= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra )


bt_cad2.place(width=323, height=63, x=553, y=397)
bt_cad1.place(width=323, height=63, x=11, y=398)
ent_prod_nome.place(width=320, height=28, x=572, y=148)
ent_prod_codfabri2.place(width=141, height=22, x=574, y=211)

ent_prod_desc.place(width=314, height=18, x=34, y=157)
ent_prod_cod.place(width=141, height=23, x=32, y=210)
ent_prod_codfabri.place(width=314, height=22, x=34, y=261)

bt_volt1.place(width=48, height=59, x=9, y=12)
lb_cad.pack()
#==================================================================================================
lb_esc= Label(frame_menu_escolha, image=menu_prod, border=0)
bt_escolha1= Button(frame_menu_escolha, image=compranovo,border=0, command=lambda: [frame_compra.pack(), frame_menu_escolha.forget()])
bt_escolha2= Button(frame_menu_escolha, image=lista,border=0, command=lambda: [frame_escolha_term.pack(), frame_menu_escolha.forget()])
bt_escolha3= Button(frame_menu_escolha, image=altera,border=0, command=lambda: [frame_altera.pack(), frame_menu_escolha.forget()])
bt_escolha4= Button(frame_menu_escolha, image=dele,border=0, command=lambda: [frame_deleta.pack(), frame_menu_escolha.forget()])
bt_escolha5= Button(frame_menu_escolha, image=saia, border=0, command=lambda: [frame_menu.pack(), frame_menu_escolha.forget()])
bt_volt2= Button(frame_menu_escolha, image=voltacmg, border=0, command=lambda: [frame_menu.pack(), frame_menu_escolha.forget()])
#==================================================================================================
lb_compra= Label(frame_compra, image=Comprar, border=0)
bt_volt3= Button(frame_compra, image=voltacmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_compra.forget()])
bt_cad_com= Button(frame_compra, image=compranovo, border=0)
ent_compra1= Entry(frame_compra, border=0, background=fundo, foreground='white', font=letra)
ent_compra2= Entry(frame_compra, border=0, background=fundo, foreground='white', font=letra)

ent_compra2.place(width=139, height=23, x=308, y=200)
ent_compra1.place(width=141, height=24, x=14, y=200)
bt_volt3.place(width=48, height=59, x=9, y=12)
bt_cad_com.place(width=224, height=45, x=52, y=295)
lb_compra.pack()

bt_escolha1.place(width=223, height=92, x=85, y=144)
bt_escolha2.place(width=223, height=92, x=330, y=143)
bt_escolha3.place(width=223, height=92, x=86, y=260)
bt_escolha4.place(width=223, height=92, x=332, y=259)
bt_escolha5.place(width=223, height=92, x=655, y=373)
bt_volt2.place(width=48, height=59, x=9, y=12)

lb_esc.pack()
# ==============================================================================================================
lb_altera= Label(frame_altera, image=alte, border=0)
bt_volt7= Button(frame_altera, image=voltacmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_altera.forget()])
bt_confirma= Button(frame_altera, image=confirma, border=0)

ent_cod_alt= Entry(frame_altera, border=0, background=fundo, foreground='white', font=letra)
ent_fab_alt= Entry(frame_altera, border=0, background=fundo, foreground='white', font=letra)
ent_des_alt= Entry(frame_altera, border=0, background=fundo, foreground='white', font=letra)

ent_cod_alt.place(width=141, height=14, x=14, y=209)
ent_fab_alt.place(width=138, height=26, x=300, y=198)
ent_des_alt.place(width=257, height=21, x=618, y=201)
bt_confirma.place(width=242, height=43, x=43, y=296)
bt_volt7.place(width=48, height=59, x=9, y=12)
lb_altera.pack()

# ==============================================================================================================
lb_escolha_lista= Label(frame_escolha_term, image=menu_lista, border=0)
bt_escolha_fab= Button(frame_escolha_term, image=fabcmg, border=0, command=lambda:[frame_lista_fab.pack(), frame_escolha_term.forget()])
bt_escolha_cli= Button(frame_escolha_term, image=clicmg, border=0, command=lambda:[frame_lista_pro.pack(), frame_escolha_term.forget()])
bt_volt5= Button(frame_escolha_term, image=voltacmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_escolha_term.forget()])

bt_escolha_cli.place(width=225, height=43, x=84, y=220)
bt_escolha_fab.place(width=225, height=43, x=84, y=170)
bt_volt5.place(width=48, height=59, x=9, y=12)
lb_escolha_lista.pack()

# ==============================================================================================================
lb_lista_fab= Label(frame_lista_fab, image=menu_fabr_list, border=0)
bt_volt4= Button(frame_lista_fab, image=voltacmg, border=0, command=lambda: [frame_escolha_term.pack(), frame_lista_fab.forget()])
bt_volt4.place(width=48, height=59, x=9, y=12)
lb_lista_fab.pack()
# ==============================================================================================================
lb_lista_cli= Label(frame_lista_pro, image=menu_fabr_list, border=0)
bt_volt6= Button(frame_lista_pro, image=voltacmg, border=0, command=lambda: [frame_escolha_term.pack(), frame_lista_pro.forget()] )


bt_volt6.place(width=48, height=59, x=9, y=12)
lb_lista_cli.pack()

# ==============================================================================================================
lb_menu = Label(frame_menu, image=menu, border=0)
bt_fab = Button(frame_menu,image=fabcmg, border=0, command=lambda: [frame_cadastro_prod.pack(), frame_menu.forget(), frame_menu_escolha.forget()])
bt_cli = Button(frame_menu,image=clicmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_menu.forget(), frame_cadastro_prod.forget()])

bt_fab.place(width=230, height=40, x=329, y=237)
bt_cli.place(width=230, height=40, x=328, y=319)
lb_menu.pack()
# ==============================================================================================================
lb_deleta= Label(frame_deleta, image=deleta, border=0)
bt_volt8= Button(frame_deleta, image=voltacmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_menu.forget(), frame_deleta.forget()])
ent_dle= Entry(frame_deleta, border=0, background=fundo, foreground='white', font=letra)
bt_dleta= Button(frame_deleta, image= dele, border=0)

ent_dle.place(width=140, height=22, x=14, y=201)
bt_dleta.place(width=225, height=45, x=44, y=295)
bt_volt8.place(width=48, height=59, x=9, y=12)
lb_deleta.pack()








janela.mainloop()
"""
Colar as linhas no código principal. OBS: a instância da classe Tk() deve ser de mesmo nome!
master.bind('<Button-1>', posiciona.inicio_place)
master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master))
master.bind('<Button-2>', lambda arg: posiciona.para_geometry(master))
"""

# Variáveis Globais
x1 = y1 = 0  # Armazenam a posição inicial de x e y

print('''Botão Esquerdo: 'place' <Clique na posição inicial e arraste até a posição final>
Botão Scroll:   'geometry' <Mostra as medidas para o posicionamento da janela> "geometry"
''')


def inicio_place(arg):
    global x1, y1
    x1 = arg.x
    y1 = arg.y


def fim_place(arg, master):
    global x1, y1
    print(f'Copiado! .place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')
    master.clipboard_clear()
    master.clipboard_append(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')


def para_geometry(master):
    print(f'Copiado! .geometry("{master.geometry()}")')
    master.clipboard_clear()
    master.clipboard_append(f'.geometry("{master.geometry()}")')