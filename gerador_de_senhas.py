from tkinter import *
import pyperclip
import random

root = Tk()
root.title("Gerador de senhas")
root['background']='white'
root.geometry("450x210")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def gerar():
    try:
        pass1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
             'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç',
             'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E',
             'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
             'F', 'G', 'H', 'J', 'K', 'L', 'Ç', 'Z', 'X', 'C',
             'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '!', '@', '#', '$', '%', '&', '*',
             '(', ')', '+', '-']
        senha = ""
        for x in range(passlen.get()):
            senha = senha + random.choice(pass1)         
            passstr.set(senha)
    except:
        root2 = Tk()
        root2.title("ERRO!")
        root2['background']='white'
        root2.geometry("250x50")
        Label(root2, text= "INSIRA UM TAMANHO VALIDO!", bg="red").pack()
def copiarclipboard():
    random_senha = passstr.get()
    pyperclip.copy(random_senha)

Label(root, text="GERADOR DE SENHAS", font="lucida 20 bold").pack()
Label(root, text= "Digite o tamanho da senha").pack()
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Gerar senha",bg = "gray", command=gerar).pack(pady=3)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Copiar senha",bg = "gray", command=copiarclipboard).pack(pady=3)
root.mainloop()
