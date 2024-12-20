from funcoes.BancoAgenda import ConexaoBancoAgenda
from funcoes.PDF_Lista.Pdf_contato import PDF_Contato
from ModulosAgenda import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class FuncoesAgenda(PDF_Contato):
     
     def Mensagem_Personalizada(self):
        messagebox.showinfo("Hello\n ",self.nome_espaco.get())
        
     def PDF_lista(self):
          banco=ConexaoBancoAgenda()
          nome_tel_lista=banco.Lista_Toda()
          #self.teste_da_lista(nome_tel_lista)
          self.Gerar_Pdf(nome_tel_lista)
          
     def ver_contato(self):
        banco=ConexaoBancoAgenda()
        verificar=banco.Buscar_Contato(self.nome_espaco.get())
        if verificar==[]:
            return True
        else:
            messagebox.showinfo("Alerta","Nome existe")  
            return False
          
     def Inserir_Contato(self):
        banco=ConexaoBancoAgenda()
        if self.nome_espaco.get()=='' or self.tel_espaco.get()=='':
               messagebox.showinfo("Alerta\n ","insera os dados do contato ")
        elif self.ver_contato():
              banco.InserirContato(self.nome_espaco.get(),self.tel_espaco.get())
              self.Limpa_Campos()
              self.Lista_Toda_Contato()
              messagebox.showinfo("Inserir\n ","inserido o contato "+self.nome_espaco.get())
       
      

     def Limpa_Campos(self):
         self.nome_espaco.delete(0,END)
         self.tel_espaco.delete(0,END)
         
     #valida se o texto passado e um numero   
     def valida_num(self,textonum):
        if int(textonum)>=0:
            return True
        else:
            return False
         
     def valida(self, texto):
        if texto=='':return True
        try:
            #value=int(texto)
            if self.valida_num(texto):
                value=len(texto)    
            
        except ValueError:
            return False
        return 0<=value <=14

     def Lista_Toda_Contato(self):
        banco=ConexaoBancoAgenda()
        self.lista.delete(*self.lista.get_children())
        lista_tree=banco.Lista_Toda()
        for i in lista_tree:
            self.lista.insert("",END,values=i)

    
     def Atualizar_Contato_Lista(self):
        banco=ConexaoBancoAgenda()
        if self.nome_espaco.get()=='' or self.tel_espaco.get()=='':
               messagebox.showinfo("Alerta\n ","insera os dados do contato ")
        else:
            if self.nom!='':
                 banco.Atualiza_Contato(
                     self.nom,
                     self.nome_espaco.get(),
                     self.tel_espaco.get()
                     )
                 self.Lista_Toda_Contato()
                 self.Limpa_Campos()
                 self.nom=""

     def Buscar_Entry_Contato(self):
        
        if self.nome_espaco.get()!="":
            banco=ConexaoBancoAgenda()
            self.lista.delete(*self.lista.get_children())
            self.nome_espaco.insert(END,"%")
            nome=self.nome_espaco.get()
            nome_retorno=banco.Buscar_Contato(nome)
            for i in nome_retorno:
                self.lista.insert("",END,values=i)
                
            self.Limpa_Campos()
        else:
            messagebox.showinfo("Alerta\n ","Campo nome vazio ")
    
     def Deletar_Contato_Lista(self):
        banco=ConexaoBancoAgenda()
        if self.nome_espaco.get()=='' or self.tel_espaco.get()=='' and self.nom=='':
            messagebox.showinfo("Alerta\n ","insera os dados do contato ")
        else:
            banco.Deleta_Contato(self.nome_espaco.get())
            messagebox.showinfo("Excluir\n ","excluido o "+self.nome_espaco.get()+" com suecesso")
            self.Lista_Toda_Contato()
            self.Limpa_Campos()
            self.nom=""

            
     def Clique_Duplo(self, event):
        self.Limpa_Campos()
        self.lista.selection()
        for n in self.lista.selection():
            col1,col2=self.lista.item(n,'values')
            self.nome_espaco.insert(END, col1)
            self.tel_espaco.insert(END, col2)
            self.nom=self.nome_espaco.get()
            
     
