import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk  # pip install pillow
import serial
import time



# criando a tela e suas predefinições

tela = ttk.Window(themename="vapor")
tela.title("INTERFACE DE CONTROLE")
tela.geometry("1000x900")




# funcoes de controle para cada botao

def conectar():
    global arduino
    global porta_inserida

    porta_inserida = entrada.get()
    
        # definir a porta e a velocidade da comunicação:
     
    baud_rate = 9600

    # fazendo a comunicação com o arduino na porta escolhida:
    try:
        arduino = serial.Serial(porta_inserida, baud_rate, timeout=1)
        print("Conexão  com o arduino foi realizada")
    except Exception as e:
        print("Erro ao conectar o arduino", e)
        exit()
    


def mover_frente():
   
    mensagem = "f"
    arduino.write((mensagem + "\n").encode()) 
    print(mensagem)

def mover_re():
    mensagem = "r"
    arduino.write((mensagem + "\n").encode()) 
    print(mensagem)

def mover_esquerda():
    mensagem = "e"
    arduino.write((mensagem + "\n").encode()) 
    print(mensagem)

def mover_direita():
    mensagem = "d"
    arduino.write((mensagem + "\n").encode()) 
    print(mensagem)


def ligar_farol():
    mensagem = "l"
    arduino.write((mensagem + "\n").encode()) 
    print(mensagem)










# estilo presonalizado para botões

style = ttk.Style()
style.configure('Custom.TButton',
                borderwidth=8,          # Define a largura da borda
                bordercolor='white',      # Define a cor da borda (pode não funcionar em todos os temas)
                foreground='black',     # Cor do texto
                # background='lightgray', # Cor de fundo (pode ser substituída pelo tema)
                relief="solid")         # Estilo da borda (flat, groove, raised, ridge, solid, sunken)







# titulo
lbl_titulo = ttk.Label(tela, text="INTERFACE DE CONTROLE ", font=("Segoe UI", 20), anchor="c")
lbl_titulo.place(x=0 , y=20, width=1000)

              
# inserir a porta serial escolhida
lbl_input = ttk.Label(tela, text="Porta Serial: ", font=("Segoe UI", 12))
lbl_input.place(x=20 , y=150)

entrada = ttk.Entry(tela)
entrada.place(x=140 , y=150)

btn_carregar = ttk.Button(tela, text="Carregar", bootstyle=SECONDARY, command=conectar)
btn_carregar.place(x=350, y=150)





# botoes do controle
btn_frente = ttk.Button(tela, text="", style='Custom.TButton', command=mover_frente)
btn_frente.place(x=450, y=350, width=80, height=80)

btn_re = ttk.Button(tela, text="", style='Custom.TButton', command=mover_re)
btn_re.place(x=450, y=650, width=80, height=80)

btn_esquerda = ttk.Button(tela, text="", style='Custom.TButton', command=mover_esquerda)
btn_esquerda.place(x=300, y=500, width=80, height=80)

btn_direita = ttk.Button(tela, text="", style='Custom.TButton', command=mover_direita)
btn_direita.place(x=600, y=500, width=80, height=80)

btn_farol = ttk.Button(tela, text="", style='Custom.TButton', command=ligar_farol)
btn_farol.place(x=463, y=515, width=50, height=50)





tela.mainloop()    