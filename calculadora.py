from tkinter import ttk
import tkinter as tk

#Ventana Principal de la app
gui = tk.Tk()

#Tamanno de la interfaz
gui.geometry('350x500')

#Titulo de la ventana
gui.title('Calculadora KT')

#Salida de texto
output = tk.Entry(gui, font = 'verdana 20', background='green')
output.grid(row = 0, column = 0, columnspan = 4, ipadx = 4, ipady = 70)

#Botones

button_on       = ttk.Button(gui, text = 'C')
button_parLeft  = ttk.Button(gui, text = '(')
button_parRigth = ttk.Button(gui, text = ')')
button_delete   = ttk.Button(gui, text = '⌫')

button_0 = ttk.Button(gui, text = '0')
button_1 = ttk.Button(gui, text = '1')
button_2 = ttk.Button(gui, text = '2')
button_3 = ttk.Button(gui, text = '3')
button_4 = ttk.Button(gui, text = '4')
button_5 = ttk.Button(gui, text = '5')
button_6 = ttk.Button(gui, text = '6')
button_7 = ttk.Button(gui, text = '7')
button_8 = ttk.Button(gui, text = '8')
button_9 = ttk.Button(gui, text = '9')

button_divide    = ttk.Button(gui, text = '/')
button_mulltiply = ttk.Button(gui, text = 'X')
button_subtract  = ttk.Button(gui, text = '-')
button_add       = ttk.Button(gui, text = '+')
button_decimal   = ttk.Button(gui, text = '.')

#Posiciones de los botones
button_on.grid(row = 1,column = 0, ipadx = 6, ipady= 20)
button_parLeft.grid(row = 1,column = 1, ipadx = 6, ipady= 20)
button_parRigth.grid(row = 1,column = 2, ipadx = 6, ipady= 20)
button_delete.grid(row = 1,column = 3, ipadx = 6, ipady= 20)

button_0.grid(row = 5, columnspan = 2, column = 0, ipadx = 50, ipady = 20)
button_1.grid(row = 4, column = 0, ipadx = 6, ipady = 20)
button_2.grid(row = 4, column = 1, ipadx = 6, ipady = 20)
button_3.grid(row = 4, column = 2, ipadx = 6, ipady = 20)
button_4.grid(row = 3, column = 0, ipadx = 6, ipady = 20)
button_5.grid(row = 3, column = 1, ipadx = 6, ipady = 20)
button_6.grid(row = 3, column = 2, ipadx = 6, ipady = 20)
button_7.grid(row = 2, column = 0, ipadx = 6, ipady = 20)
button_8.grid(row = 2, column = 1, ipadx = 6, ipady = 20)
button_9.grid(row = 2, column = 2, ipadx = 6, ipady = 20)

button_divide.grid(row = 2 , column = 3, ipadx = 6, ipady = 20)
button_mulltiply.grid(row = 3 , column = 3, ipadx = 6, ipady = 20)
button_subtract.grid(row = 4 , column = 3, ipadx = 6, ipady = 20)
button_add.grid(row = 5, column = 3, ipadx = 6, ipady = 20)
button_decimal.grid(row = 5, column = 2, ipadx = 6, ipady = 20)

#Loop principal de la app
gui.mainloop()