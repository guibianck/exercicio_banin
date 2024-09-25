import sqlite3
conector = sqlite3.connect("academia.db") #faz a conexão e cria o arquivo academia.db, se não existir

#cria um cursor para executar os comandos sql
cursor = conector.cursor()


#se a tabela alunos existe, então elimine-a
try:
    sql = "drop table alunos"
    cursor.execute(sql)
    sql = "drop table professores"
    cursor.execute(sql)
except sqlite3.OperationalError:
    pass #se o erro ocorrer, não queremos fazer nada

#_id é um nome padrão de chave primária do Android
#cria a tabela alunos
sql = """
    create table alunos (
        _id INTEGER PRIMARY KEY AUTOINCREMENT, 
        MATRICULA INTEGER,
        NOMEALU STRING,
        IDADE INTEGER,
        PESO NUMERIC)
"""
cursor.execute(sql)
sql = """
    create table professores(
        _id INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMEPROF STRING,
        ESPECIALIDADE STRING)
"""
cursor.execute(sql)

sql = """
    insert into alunos(MATRICULA, NOMEALU, IDADE,PESO) values (123,"Isabela",20,52.0),(124,"Guilherme",20,110.0),(125,"Gustavo",20,70.2)
"""

cursor.execute(sql)
sql = """
    insert into professores(NOMEPROF,ESPECIALIDADE) values ("Adilson","Medico"),("Baninho","Zoeira"),("Humberto","Retorno de feedback")
"""
cursor.execute(sql)
conector.commit()


cursor.close()
conector.close()


print('Fim do programa')
