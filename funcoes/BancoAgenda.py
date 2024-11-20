import mysql.connector


class ConexaoBancoAgenda:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',database='ContatosBanco',user='root',password='')
        self.cursor=self.con.cursor()
   
    def Desconecta(self):
         if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("Encerrando....")



    def Conecta(self):
        try:
            if self.con.is_connected():
                db_info=self.con.get_server_info()
                print("Connectda ao banco ",db_info)
                print("Sucesso ")
          
        except mysql.connector.Error as erro:
            print("falha->"+ erro)
    def testar(self):
        try:
            self.Conecta()
            self.Desconecta()
          
        except mysql.connector.Error as erro:
            print("falha->"+ erro)
    def InserirContato(self,nome,telefone):
        try:
           self.Conecta()
           dads='\''+nome+'\','+'\''+telefone+'\''+');'
           comandoin="""INSERT INTO contatosAgenda(nomeAgenda,numTel) VALUES("""
           print(comandoin+dads)
           self.cursor.execute(comandoin+dads)
           self.con.commit()
           print("inserido com sucesso")
           
        except mysql.connector.Error as erro:
           print("falha->"+ erro)
        finally:
            self.Desconecta()
    def Lista_Toda(self):
        try:
            self.Conecta()
            comando="""SELECT * FROM contatosAgenda ORDER BY nomeAgenda ASC"""
            self.cursor.execute(comando)
            retorna=self.cursor.fetchall()
            #print(retorna)
          
           
        except mysql.connector.Error as erro:
            print("falhou a seleção da lista total ", erro)
        finally:
            self.Desconecta()
            return retorna

    def Pesquisar_Nome(self,nome):
        try:   
            self.Conecta()
            comando2="""SELECT * FROM contatosAgenda WHERE nomeAgenda="""
            dado1=nome
            self.cursor.execute(comando2+dado1)
            retorna=self.cursor.fetchall()
            print("Sucesso ",retorna)
            return retorna
        except mysql.connector.Error as erro:
            print("falhou  o comando buscar nome do contato", erro)
        finally:
            self.Desconecta()

        
    def Buscar_Contato(self,dado):
        try:   
            self.Conecta()
            comando2="""SELECT * FROM contatosAgenda WHERE nomeAgenda LIKE %s ORDER BY nomeAgenda ASC"""
            dado1=(dado,)
            self.cursor.execute(comando2,dado1)
            retorna=self.cursor.fetchall()
            print("Sucesso ", retorna)
            return retorna
        except mysql.connector.Error as erro:
            print("falhou  o comando buscar ", erro)
        finally:
            self.Desconecta()
