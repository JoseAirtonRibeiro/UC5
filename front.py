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
saia = PhotoImage(file='Foto/saia.png')
lista = PhotoImage(file='Foto/lista.png')
compranovo = PhotoImage(file='Foto/compra1.png')
dele = PhotoImage(file='Foto/deleta.png')
altera = PhotoImage(file='Foto/altera.png')
clicmg = PhotoImage(file='Foto/bt_cliente.png')
fabcmg = PhotoImage(file='Foto/bt_fabri.png')
voltacmg = PhotoImage(file='Foto/bt_back.png')
menu = PhotoImage(file='Foto/Menu.png')
menu_esc = PhotoImage(file='Foto/Menu_Produto.png')
cadastro = PhotoImage(file='Foto/Cadastro.png')
comprar = PhotoImage(file='Foto/Comprar.png')
alte = PhotoImage(file='Foto/Alterar.png')
deleta = PhotoImage(file='Foto/Deletar.png')
menu_prod_list = PhotoImage(file='Foto/SE_Produto.png')
compra = PhotoImage(file='Foto/SE_Fabricante.png')
menu_lista = PhotoImage(file='Foto/Menu_Escolha.png')
#==================================================================================================
lb_cad= Label(frame_cadastro_prod, image=cadastro, border=0)
bt_volt1= Button(frame_cadastro_prod, image=voltacmg, border=0, command=lambda: [frame_menu.pack(), frame_cadastro_prod.forget()])
ent_prod_desc= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)
ent_prod_cod= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)
ent_prod_codfabri= Entry(frame_cadastro_prod, border=0, background=fundo, foreground='white', font=letra)






ent_prod_desc.place(width=314, height=18, x=34, y=157)
ent_prod_cod.place(width=141, height=23, x=32, y=210)
ent_prod_codfabri.place(width=314, height=22, x=34, y=261)

bt_volt1.place(width=-61, height=-68, x=62, y=69)
lb_cad.pack()
#==================================================================================================
lb_esc= Label(frame_menu_escolha, image=menu_esc, border=0)
bt_escolha1= Button(frame_menu_escolha, image=compranovo, border=0)
bt_escolha2= Button(frame_menu_escolha, image=lista, border=0)
bt_escolha3= Button(frame_menu_escolha, image=altera, border=0)
bt_escolha4= Button(frame_menu_escolha, image=dele, border=0)
bt_escolha5= Button(frame_menu_escolha, image=saia, border=0)
bt_volt2= Button(frame_menu_escolha, image=voltacmg, border=0)

bt_escolha1.place(width=225, height=94, x=85, y=144)
bt_escolha2.place(width=227, height=96, x=330, y=143)
bt_escolha3.place(width=223, height=92, x=86, y=260)
bt_escolha4.place(width=223, height=94, x=332, y=259)
bt_escolha5.place(width=223, height=92, x=655, y=373)
bt_volt2.place(width=-63, height=-75, x=65, y=77)

lb_esc.pack()





























# ==============================================================================================================
# tela seleção de login
# labels
lb_menu = Label(frame_menu, image=menu, border=0)
bt_fab = Button(frame_menu,image=fabcmg, border=0, command=lambda: [frame_cadastro_prod.pack(), frame_menu.forget(), frame_menu_escolha.forget()])
bt_cli = Button(frame_menu,image=clicmg, border=0, command=lambda: [frame_menu_escolha.pack(), frame_menu.forget(), frame_cadastro_prod.forget()])

bt_fab.place(width=240, height=48, x=330, y=239)
bt_cli.place(width=242, height=49, x=328, y=319)


lb_menu.pack()










janela.mainloop()