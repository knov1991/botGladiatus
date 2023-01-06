from tkinter import *
from threading import *
from time import sleep
from tkinter import ttk

valor = 0
start = False

class multi_threading():
    # Call work function
    def bot_start():
      t1=Thread(target=iniciar_bot)
      t1.start()
    def bot_value():
      t1=Thread(target=aumentar_valor)
      t1.start()

def iniciar_bot():
  global start, month_cb
  if start == True:
    print('parar bot')
    btnIniciar['text'] = 'INICIAR BOT'
    start = False
  else:
    print('inicar bot')
    btnIniciar['text'] = 'PARAR BOT'
    start = True
  while start == True:
    print('valor:', valor)
    sleep(1)
    print(month_cb.get())
    sleep(2)
    print(month_cb.get())

def aumentar_valor():
  global valor
  valor += 1

#cores
corFundo = '#dde'
corTexto = '#c0c'
corAlerta = '#f00'
corInfo = '#070'
#interface
app=Tk()
app.title('TURIM FERRARI')
app.geometry('800x600')
app.resizable(False,False)
app.configure(background=corFundo)
#campo de texto para variaveis
#ValorInicial
Label(app,text='Valor-Inicial',background=corFundo,foreground=corTexto,anchor=W).place(x=10,y=15,width=80,height=20)
campoValorInicial=Entry(app)
campoValorInicial.place(x=20,y=35,width=50,height=20)

#botao para iniciar o BOT
btnIniciar = Button(app,text='INICIAR BOT',command=lambda: [multi_threading.bot_start()])
btnIniciar.place(x=50,y=120,width=200,height=60)

#btn aumentar valor
btnValor = Button(app,text='AUMENTAR VALOR',command=lambda: [multi_threading.bot_value()])
btnValor.place(x=250,y=120,width=200,height=60)


# create a combobox
lista_items = ['opa', 'blz']
month_cb = ttk.Combobox(app, values=lista_items)
# prevent typing a value
month_cb['state'] = 'readonly'
month_cb.current(0)

# place the widget
#month_cb.pack(fill=tk.X, padx=5, pady=5)
month_cb.pack()



app.mainloop()