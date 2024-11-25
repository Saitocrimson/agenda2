from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class PDF_Contato:
    def teste_da_lista(self,lista_total):
        for t in lista_total:
            print(t[1])
        print(lista_total)
    def Gerar_Pdf(self,lista_total):
        #Nota;para salvar em outro lugar no inicio precisa colocar(se for windows) o \\ ex:.\\funcoes\PDF_Lista\contatos.pdf"
        self.arq=canvas.Canvas(".\contatos.pdf",pagesize=A4)
        self.arq.setFont("Helvetica-Bold",24)
        self.arq.drawString(190, 790,'--------Contatos-------')
        self.arq.setFont("Helvetica",15)
        eixoX=100
        eixoX2=350
        eixoY=760
        for t in lista_total:
            self.arq.drawString(eixoX,eixoY,'Nome: '+t[0])
            self.arq.drawString(eixoX2,eixoY,"Telefone:  "+t[1])
            self.arq.line(100,eixoY,520,eixoY)
            eixoY-=40
            
        self.arq.save()
        print("ok")



