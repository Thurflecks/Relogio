import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title("Relógio")
root.geometry("300x300")
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


saudacao = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 22))
saudacao.pack()
data = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 24))
data.place(relx=0.5, y=100, anchor="center")
horas = Label(root, bg = '#000', fg = '#e827ea',  font=('gabriola', 64, 'bold'))
horas.place(relx=0.5, y= 200, anchor='center')

get_saudacao()
get_data()
get_horas()

root.mainloop()