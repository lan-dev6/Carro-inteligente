import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk  # pip install pillow

import serial
import time

tela = ttk.Window(themename="cosmo")
tela.title("INTERFACE DE CONTROLE")
tela.geometry("1000x900")


lbl_titulo = ttk.Label(tela, text="INTERFACE DE CONTROLE: ", font=("Segoe UI", 20), anchor="c")
lbl_titulo.place(x=0 , y=20, width=1000)


lbl_input = ttk.Label(tela, text="Porta Serial: ", font=("Segoe UI", 12))
lbl_input.place(x=20 , y=150)

entrada = ttk.Entry(tela)
entrada.place(x=140 , y=150)


btn_carregar = ttk.Button(tela, text="Carregar", bootstyle=SUCCESS, command="")
btn_carregar.place(x=350, y=150)




btn_frente = ttk.Button(tela, text="⬆️", bootstyle=SUCCESS, style="Grande.TButton",command="")
btn_frente.place(x=350, y=550, width=100, height=100)






tela.mainloop()






















# definir a porta e a velocidade da comunicação:
porta = input("Selecione a porta: ")
baud_rate = 9600

# fazendo a comunicação com o arduino na porta escolhida:
try:
    arduino = serial.Serial(porta, baud_rate, timeout=1)
    print("Conexão  com o arduino foi realizada")
except Exception as e:
    print("Erro ao conectar o arduino", e)
    exit()


































# loop principal da conversa entre o computador e o arduino:

while True:
    mensagem = input('---> ')
    arduino.write((mensagem + "\n").encode()) #envia e transforma a string em bytes para a comunicacao serial



































