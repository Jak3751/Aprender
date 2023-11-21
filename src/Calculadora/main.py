from tkinter import *
from tkinter import ttk

# Definindo cores - Colour picker
cor1 = "#3b3b3b"  # Preto
cor2 = "#feffff"  # Branco
cor3 = "#38576b"  # Azul
cor4 = "#ECEFF1"  # Cinza
cor5 = "#FFAB40"  # Laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


# Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Botões
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4)
b_1.place(x=0, y=0)  # Direcinando botão, vertical/horizontal
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4)
b_2.place(x=90, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5)
b_3.place(x=177, y=0)

janela.mainloop()
