from ModulosAgenda import *


class FuncoesAgenda:
     def Mensagem_Personalizada(self):
        messagebox.showinfo("Hello\n ",self.nome_espaco.get())
     def Inserir_Contato(self):
        messagebox.showinfo("Inserir\n ","inserido o contato "+self.nome_espaco.get())

     def Limpa_Campos(self):
         self.nome_espaco.delete(0,END)
         self.tel_espaco.delete(0,END)
         
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



