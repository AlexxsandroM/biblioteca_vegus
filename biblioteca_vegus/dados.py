import sqlite3

# Conectar ao banco de dados ou criar um novo banco de dados
con = sqlite3.connect('dados.db')


# Criar tabela de Livros
con.execute('CREATE TABLE IF NOT EXISTS livros(\
            id INTEGER PRIMARY KEY,\
            titulo TEXT,\
            autor TEXT,\
            editora TEXT,\
            ano_publicacao INTEGER,\
            isbn TEXT)')  

# Criar tabela de Usuarios
con.execute('CREATE TABLE IF NOT EXISTS usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXT,\
            sobrenome TEXT,\
            endereco TEXT,\
            email TEXT,\
            telefone TEXT)') 

# Criar tabela de emprestimo
con.execute('CREATE TABLE IF NOT EXISTS emprestimos(\
            id INTEGER PRIMARY KEY,\
            id_livro INTEGER,\
            id_usuario INTEGER,\
            data_emprestimo TEXT,\
            data_devolucao TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))') 




