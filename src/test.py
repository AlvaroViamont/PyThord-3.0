import tkinter as tk
from tkinter import messagebox

OUTER_SPACE = '#4A5859'

root = tk.Tk()
root.configure
root.configure(background=OUTER_SPACE)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))
root.title("SAZPF/Pagina de Inicio")
root.state('zoomed')


battery = {
    'b1': 50,
    'b2': 50,
    'b3': 10,
    'b4': 50
}

def activar_btn ():
    if all(value > 25 for value in battery.values()):
        messagebox.showinfo('Exito', 'Se produjo un éxito')
    else:
        messagebox.showwarning('Bateria Baja', 'Carga los módulos')

boton = tk.Button(root, text='click', width=20, height=5, command=activar_btn)
boton.pack(pady=20)


root.mainloop()