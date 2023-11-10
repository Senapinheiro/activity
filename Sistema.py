import sqlite3

class Aluno():

    def __init__(self,nome,CPF,telefones):
        self.nome = nome
        self.CPF = CPF
        self.telefones = telefones

    def adicionar(self):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT COUNT(*) FROM Endereco").fetchone()[0] + 1

        cursor.execute("INSERT INTO Aluno (nome,CPF,id_Endereco) VALUES('"+
        self.nome+"','"+self.CPF+"',%i)" %(count))
        con.commit()

        cursor.execute("INSERT INTO Endereco(idEndereco) VALUES(%i)" %(count))
        print(count)


        count = cursor.execute("SELECT COUNT(*) FROM Telefone").fetchone()[0] + 1

        for i in range(0,len(self.telefones)):
            cursor.execute("INSERT INTO Telefone(idTelefone,numero,cpfAluno) VALUES(%i,'"%(count+i)+self.telefones[i]+"','"+self.CPF+"')")
            con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def alterarNome(nome,CPF):
        con = sqlite3.connect("./SGN.bd")
        cursor = con.cursor()

        cursor.execute("UPDATE Aluno SET nome = '"+
        nome+"' WHERE CPF like '"+CPF+"'")
        con.commit()

        con.close()

    @staticmethod
    def consultar(CPF):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Aluno WHERE CPF like '"+CPF+"'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Aluno não cadastrado!'
    
    @staticmethod
    def remover(CPF):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.execute("DELETE FROM Aluno WHERE CPF like '"+CPF+"'")
        con.commit()


        cursor.close()
        con.close()

    #Método que adiciona 5 entradas
    def addFive(alunos):
        for i in range(5):
            Aluno.adicionar(alunos[i])

    #Método que consulta string
    def consultarStr(nome):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Aluno WHERE Nome like '"+nome+"'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Nenhum aluno encontrado!'

class Professor():

    def __init__(self,nome,CPF,telefones):
        self.nome = nome
        self.CPF = CPF
        self.telefones = telefones

    def adicionar(self):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT COUNT(*) FROM Endereco").fetchone()[0] + 1

        cursor.execute("INSERT INTO Professor (nome,CPF,id_Endereco) VALUES('"+
        self.nome+"','"+self.CPF+"',%i)" %(count))
        con.commit()

        cursor.execute("INSERT INTO Endereco(idEndereco) VALUES(%i)" %(count))
        print(count)

        count = cursor.execute("SELECT COUNT(*) FROM Telefone").fetchone()[0] + 1

        for i in range(0,len(self.telefones)):
            cursor.execute("INSERT INTO Telefone(idTelefone,numero,cpfProfessor) VALUES(%i,'"%(count+i)+self.telefones[i]+"','"+self.CPF+"')")
            con.commit()
        

        cursor.close()
        con.close()

    @staticmethod
    def alterarNome(nome,CPF):
        con = sqlite3.connect("./SGN.bd")
        cursor = con.cursor()

        cursor.execute("UPDATE Professor SET nome = '"+
        nome+"' WHERE CPF like '"+CPF+"'")
        con.commit()

        con.close()

    @staticmethod
    def consultar(CPF):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Professor WHERE CPF like '"+CPF+"'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Professor não cadastrado!'
    
    @staticmethod
    def remover(CPF):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.execute("DELETE FROM Professor WHERE CPF like '"+CPF+"'")
        con.commit()


        cursor.close()
        con.close()

    #Método que adiciona 5 entradas
    def addFive(professores):
        for i in range(5):
            Professor.adicionar(professores[i])


    #Método que consulta string
    def consultarStr(nome):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Aluno WHERE Nome like '"+nome+"'").fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Nenhum professor encontrado!'


class Endereco():
    def __init__(self,rua,numero,bairro,CEP,complemento):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.CEP = CEP
        self.complemento = complemento

    def adicionar(self):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        count = cursor.execute("SELECT COUNT(*) FROM Endereco").fetchone()[0] + 1

        cursor.execute("INSERT INTO Endereco(idEndereco,rua,numero,bairro,CEP,complemento) VALUES(%i,'"%(count)+self.rua+"','"+self.numero+"','"+self.bairro+"','"+
        self.CEP+"','"+self.complemento+"')")
        con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def alterar(id,NovaRua,NovoNumero,NovoBairro,NovoCEP,NovoComplemento):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.execute("UPDATE Endereco SET rua = '"+NovaRua+"',"+
        "numero = '"+NovoNumero+"', bairro = '"+NovoBairro+"',"+
        "CEP = '"+NovoCEP+"', complemento = '"+NovoComplemento+
        "' WHERE idEndereco = %i"%(id))
        con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def remover():
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        cursor.close()
        con.close()

    #Método que adiciona 5 entradas
    def addFive(enderecos):
        for i in range(5):
            Endereco.adicionar(enderecos[i])


    @staticmethod
    def consultar(id):
        con = sqlite3.connect("./SGN.db")
        cursor = con.cursor()

        informacoes = cursor.execute("SELECT * FROM Endereco WHERE idEndereco = %i"%(id)).fetchall()

        cursor.close()
        con.close()
        if len(informacoes) != 0:
            return informacoes
        else:
            return 'Endereço inexistente!'








#teste de consulta
print(Aluno.consultar('001'))
print(Aluno.consultar('321'))
print(Professor.consultar('444'))
print(Professor.consultar('888'))

#teste da função de adicionar 5 entradas
alu1 = Aluno('Meyre','423',['321', '541'])
alu2 = Aluno('Marcos','999',['427'])
alu3 = Aluno('Abel','135',['887', '462'])
alu4 = Aluno('Helena','032',['155'])
alu5 = Aluno('Marcos','888',['321'])
alunos = [alu1, alu2, alu3, alu4, alu5]

Aluno.addFive(alunos)

#inserção de endereço
End = Endereco('Av. Amaro','107','Parquelândia','896','Null')
Endereco.adicionar(End)

#inserção de alunos
Al = Aluno('Letícia', '321', ['231', '432'])
Aluno.adicionar(Al)

#novo teste de consulta
print(Aluno.consultar('001'))
print(Aluno.consultar('321'))
print(Professor.consultar('444'))
print(Professor.consultar('888'))

#teste da função de consultar pela string
print(Aluno.consultarStr('Marcos'))

