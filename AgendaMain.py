from tkinter import *
from tkinter import ttk
from tkinter import tix
from  tkinter import messagebox

root=tix.Tk()

class AgendaMain():
     def __init__(self):
        self.root=root
        self.tela()
        self.divisao_telas()
        self.Labels_Dados()
        self.Entry_Dados()
        root.mainloop()
     def mensagem_campo_vazio(self,msg):
        messagebox.showinfo("Aviso!!!\n ", msg)
     def tela(self):
        'titulo'
        self.root.title("Agenda")
        'fundo'
        self.root.configure(background='#1e3743')
        'tamanho'
        self.root.geometry("500x456")
        'tamanho diminuir aumentar(HOZ/VERT)'
        self.root.resizable(False, False)
     def divisao_telas(self):
        #tela grande
        self.frames=Frame(self.root,bd=4,bg='white',highlightbackground='black',highlightthickness=2)
        self.frames.place(relx=0.1, rely=0.05, relwidth=0.80, relheight=0.25)

        #tela pequena
        self.frames2=Frame( self.root,bg='black',highlightbackground='white',highlightthickness=2)
        self.frames2.place(relx=0.1, rely=0.4, relwidth=0.80, relheight=0.5)
     def Labels_Dados(self):
        #nome
        self.lab_cod2=Label(self.frames, text="Nome",bg="white",fg='black',font=('verdana',8,'bold'))
        self.lab_cod2.place(relx=0.03, rely=0.01)
        #telefone
        self.lab_cod4=Label(self.frames, text="Telefone/celular",bg='white',fg='black',font=('verdana',8,'bold'))
        self.lab_cod4.place(relx=0.03, rely=0.4)
     def Entry_Dados(self):
        #nome
        self.nome_espaco=Entry(self.frames,bg='purple')
        self.nome_espaco.place(relx=0.03, rely=0.2,relwidth=0.9, relheight=0.2)
        #espaco
        self.tel_espaco=Entry(self.frames,bg='purple')
        self.tel_espaco.place(relx=0.03, rely=0.6,relwidth=0.4, relheight=0.2)

       
AgendaMain()
