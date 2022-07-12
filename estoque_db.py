import mysql.connector as ms 
import mysql.connector


class Backend:
    def __init__(self):
        self.conta = Conta()

    def Cadastrar(self, codigo, descricao, quantidade, email):
        if messagebox.askyesno('confirmar', 'salvar produto?'):
            self.Data.Cadastrar(cpf.get(), nome.get(), datanasc.get(), 'M', email.get(), senha.get(), 0)
            cpf.delete(0, 'end')
            nome.delete(0, 'end')
            datanasc.delete(0, 'end')
            email.delete(0, 'end')
            senha.delete(0, 'end')
            conf.delete(0, 'end')
            c_m.deselect()
            c_f.deselect()
            c_a.deselect()
            c_e.deselect()
            frame_func.pack()
            frame_cadas.forget()
        else:
            pass

    def Entrar_func(self, entry_func, entry_senha, frame_cadas, frame_func):
        if self.Data.Check_func(entry_func, entry_senha):
            frame_cadas.pack()
            frame_func.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta invalida, tente novamente')

    def Entrar_cli(self, entry_cpf, entry_senha, frame_conta, frame_entrar, frame_cli):
        if self.Data.Check_cli(entry_cpf, entry_senha):
            frame_conta.pack()
            frame_entrar.forget()
            frame_cli.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta desconhecida, tente novamente')
    
    def Saque(self, cpf, saldo, frame1, frame2, en_saque):
        if self.conta.verifica(cpf, saldo):
            self.conta.saque(cpf, saldo)
            messagebox.showinfo('Saque Aceito', f'O valor de R${saldo} foi retirado da sua conta!')
            frame1.pack()
            frame2.forget()
            en_saque.delete(0, 'end')
        else:
            messagebox.showerror('Saque Negado','Saldo insuficiente!')
            frame1.pack()
            frame2.forget()
            en_saque.delete(0, 'end')

    def Depo(self,cpf, saldo, frame1, frame2, en_depo):
        self.conta.deposito(cpf, saldo)
        messagebox.showinfo('Depositar', f'O valor de R${saldo} foi adicionado na sua conta!')
        frame1.pack()
        frame2.forget()
        en_depo.delete(0, 'end')