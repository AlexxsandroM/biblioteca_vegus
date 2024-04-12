from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

from tkinter import messagebox

# Colocando funções da view

from view import * 


# cores

co0 = "#2e2d2b" #Preta
co1 = "#feffff" #Branca
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra
co5 = "#e06636" #-Profit
co6 = "#A62B1F" #Vermelho
co7 = "#3fbfb9" #Verde
co8 = "#263238" #+Verde
co9 = "#e9edf5" #+Verde
co10 = "#6e8faf" 
co11 = "#f2f4f2"


# Criando janela ---------------------------
janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames ---------------------------------------

frame_cima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
frame_cima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frame_esquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frame_esquerda.grid(row=1, column=0, sticky=NSEW)

frame_direita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frame_direita.grid(row=1, column=1, sticky=NSEW)

# Logo ----------------------------------------
# Abrindo a imagem
app_img = Image.open('image/TsuBranco.png')# COLOCAR LOGO DA VEGUS AQUI
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_logo_texto = Label(frame_cima, text="Bem-vindo à biblioteca Vegus", compound=LEFT, padx=5, anchor=NW,font=('Verdana 15 bold'), bg=co6, fg=co1)
app_logo_texto.place(x=50, y=7)

app_linha = Label(frame_cima, width=770, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)



# Novo usuario
def novo_usuario():

    global img_salvar

    def add():
        firt_name = entrada_primeiro_nome.get()
        last_name = entrada_sobrenome.get()
        address = entrada_endereco.get()
        email = entrada_email.get()
        phone = entrada_numero.get()

        lista = [firt_name, last_name, phone]

        # Verificando caso algum campo estaja vazio ou não
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inseririndo os dados no banco de dados 
        insert_user(firt_name, last_name, address, email, phone)

        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso')

        # Limpando os campos de entradas
        entrada_primeiro_nome.delete(0,END)
        entrada_sobrenome.delete(0,END)
        entrada_endereco.delete(0,END)
        entrada_email.delete(0,END)
        entrada_numero.delete(0,END)
             

    app_ = Label(frame_direita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frame_direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    label_primeiro_nome = Label(frame_direita, text="Primeiro nome*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    label_primeiro_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    entrada_primeiro_nome = Entry(frame_direita, width=25, justify='left', relief='solid')
    entrada_primeiro_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    label_sobrenome = Label(frame_direita, text="Sobrenome*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    label_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    entrada_sobrenome = Entry(frame_direita, width=25, justify='left', relief='solid')
    entrada_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    label_endereco = Label(frame_direita, text="Endereço do usuário",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    label_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    entrada_endereco = Entry(frame_direita, width=25, justify='left', relief='solid')
    entrada_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    label_email = Label(frame_direita, text="Endereço de email",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    label_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    entrada_email = Entry(frame_direita, width=25, justify='left', relief='solid')
    entrada_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    label_numero = Label(frame_direita, text="Número de telefone*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    label_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    entrada_numero = Entry(frame_direita, width=25, justify='left', relief='solid')
    entrada_numero.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão salvar
    img_salvar = Image.open('image/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frame_direita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, sticky=NSEW,pady=5)


# Ver usuarios
def ver_usuarios():

    app_ = Label(frame_direita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frame_direita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados =  get_users()

   

# Função para controlar o Menu --------------------------------
def control(i):

    # Novo usuario
    if i == 'novo_usuario':
        for widget in frame_direita.winfo_children():
            widget.destroy()

        # Chamando a função novo usuario
        novo_usuario() 





# Menu -------------------------------------
# Novo usuario
img_usuario = Image.open('image/add.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frame_esquerda,command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text=' Novo usuario', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW,padx=5 ,pady=6)

# Novo livro
img_novo_livro = Image.open('image/add.png')
img_novo_livro = img_novo_livro.resize((18,18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frame_esquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text=' Novo livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW,padx=5 ,pady=6)

# Ver livros
img_ver_livro = Image.open('image/biblioteca.png')
img_ver_livro = img_ver_livro.resize((20,20))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frame_esquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todos livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW,padx=5 ,pady=6)

# Ver usuarios
img_ver_usuario = Image.open('image/usuarios.png')
img_ver_usuario = img_ver_usuario.resize((18,18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frame_esquerda, image=img_ver_usuario, compound=LEFT, anchor=NW, text=' Exibir todos usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW,padx=5 ,pady=6)

# Realizar um emprestimo
img_imprestimo = Image.open('image/add.png')
img_imprestimo = img_imprestimo.resize((18,18))
img_imprestimo = ImageTk.PhotoImage(img_imprestimo)
b_imprestimo = Button(frame_esquerda, image=img_imprestimo, compound=LEFT, anchor=NW, text=' Realizar um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_imprestimo.grid(row=4, column=0, sticky=NSEW,padx=5 ,pady=6)

# Devolução de um emprestimo
img_devolucao = Image.open('image/atualizar.png')
img_devolucao = img_devolucao.resize((16,16))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frame_esquerda, image=img_devolucao, compound=LEFT, anchor=NW, text=' Devolução de um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=5, column=0, sticky=NSEW,padx=5 ,pady=6)

# Livros emprestados no momento
img_livros_emprestados = Image.open('image/emprestadosmomento.png')
img_livros_emprestados = img_livros_emprestados.resize((16,16))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frame_esquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW,padx=5 ,pady=6)





janela.mainloop()
