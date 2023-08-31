import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title("Relógio")
root.iconbitmap("clock1.ico")
root.geometry("600x300")
root.maxsize(600, 300)
root.minsize(600, 300)
root.configure(background='#000')


def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text = 'Olá, ' + nome_usuario)
 
def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text= data_atual)   
    
def get_horas():
   hora_atual = strftime('%H:%M:%S')
   horas.config(text=hora_atual)
   horas.after(1000, get_horas)


saudacao = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 18))
saudacao.pack()
data = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 22))
data.pack(pady=2)
horas = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 64, 'bold'))
horas.pack()

get_saudacao()
get_data()
get_horas()

root.mainloop()