from ModulosAgenda import *
from funcoes.FuncoesAgenda import FuncoesAgenda
from cores.Cores import CoresAgenda

root=tix.Tk()


class AgendaMain(FuncoesAgenda,CoresAgenda):
     def __init__(self):
        self.root=root
        self.tela()
        self.validar()
        self.divisao_telas()
        self.Labels_Dados()
        self.Entry_Dados()
        self.Botao_Dados()
        self.Listar_Tab_Contatos()
        self.Lista_Toda_Contato()
        root.mainloop()
     
     def tela(self):
        'titulo'
        self.root.title("Agenda")
        'fundo'
        self.root.configure(background=self.laranja_background())
        'tamanho'
        self.root.geometry("500x456")
        'tamanho diminuir aumentar(HOZ/VERT)'
        self.root.resizable(False, False)
     def divisao_telas(self):
        #tela grande
        self.frames=Frame(self.root,bd=4,bg=self.marrom_frame1(),highlightbackground='black',highlightthickness=2)
        self.frames.place(relx=0.1, rely=0.05, relwidth=0.80, relheight=0.25)

        #tela pequena
        self.frames2=Frame( self.root,bg='black',highlightbackground='white',highlightthickness=2)
        self.frames2.place(relx=0.1, rely=0.4, relwidth=0.80, relheight=0.5)
     def Labels_Dados(self):
        #nome
        self.lab_cod2=Label(self.frames, text="Nome",bg=self.marrom_frame1(),fg='black',font=('verdana',8,'bold'))
        self.lab_cod2.place(relx=0.03, rely=0.01)
        #telefone
        self.lab_cod4=Label(self.frames, text="Telefone/celular",bg=self.marrom_frame1(),fg='black',font=('verdana',8,'bold'))
        self.lab_cod4.place(relx=0.03, rely=0.4)
     def Entry_Dados(self):
        #nome
        self.nome_espaco=Entry(self.frames,bg=self.laranja_entry())
        self.nome_espaco.place(relx=0.03, rely=0.2,relwidth=0.5, relheight=0.2)
        #espaco
        self.tel_espaco=Entry(self.frames,bg=self.laranja_entry(),validate="key",validatecommand=self.vcm2 )
        self.tel_espaco.place(relx=0.03, rely=0.6,relwidth=0.4, relheight=0.2)

     def Botao_Dados(self):
        #bg=background,fg=cor de letra
        #busca
        self.btn_buscar=Button(self.frames, text="Pesquisar",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'),command=self.Buscar_Entry_Contato)
        self.btn_buscar.place(relx=0.6,rely=0.2, relheight=0.2)
        #limpar
        self.btn_limpar=Button(self.root, text="limpar",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'),command=self.Limpa_Campos)
        self.btn_limpar.place(relx=0.15,rely=0.33,relwidth=0.15, relheight=0.06 )
        #inserir
        self.btn_inserir=Button(self.root, text="inserir",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'),command=self.Inserir_Contato)
        self.btn_inserir.place(relx=0.34,rely=0.33,relwidth=0.15,relheight=0.06 )

        #excluir
        self.btn_excluir=Button(self.root, text="excluir",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'))
        self.btn_excluir.place(relx=0.52,rely=0.33, relwidth=0.15,relheight=0.06)
        #atualizar
        self.btn_atualiza=Button(self.root, text="atualizar",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'),command=self.Mensagem_Personalizada)
        self.btn_atualiza.place(relx=0.7,rely=0.33, relheight=0.06)
        #recarrega lista
        self.btn_recarrega=Button(self.root, text="Listar",bd=4,bg=self.laranja_botao_fora(),fg="black",font=('verdana',8,'bold'),command=self.Lista_Toda_Contato)
        self.btn_recarrega.place(relx=0.34,rely=0.92,relwidth=0.15,relheight=0.06)
        
     def validar(self):
        self.vcm2=(self.root.register(self.valida),'%P')
        
     def Listar_Tab_Contatos(self):
        self.lista=ttk.Treeview(self.frames2,height=3,column=('co1','co2'))
        self.lista.heading("#0",text="")
        self.lista.heading("#1",text="Nome")
        self.lista.heading("#2",text="Telefone")
        self.lista.column("#0",width=1,stretch=NO)
        self.lista.column("#1",width=50)
        self.lista.column("#2",width=50)
        self.lista.place(relx=0.01, rely=0.01, relwidth=0.93, relheight=0.97)
        self.scrollB=Scrollbar(self.frames2,orient='vertical')
        self.lista.configure(yscroll=self.scrollB.set)
        self.scrollB.place(relx=0.95, rely=0.01, relwidth=0.04, relheight=0.97)
        self.lista.bind("<Double-1>", self.Clique_Duplo)


AgendaMain()
