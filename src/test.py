import tkinter as tk
import time
from paths import get_json_to_dict
from controllers. canvas_draw import PlotCanvas

report = get_json_to_dict('4382916', '11102024195017.json')

x = report['RDTime(ms)']
y1 = report['RDSagital']
y2 = report['RISagital']

def dibujar():
    canvas.draw_axes()
    canvas.draw_grid()
    xn1 = 0
    yn1 = 0
    xn2 = 0
    yn2 = 0
    for i in range(len(x)-1):
        if i == 0:
            xn1, yn1 = canvas.normalize_list_data(x[i], y1[i], len(x))
            xn1, yn1 = canvas.draw_function(x[i], y1[i], len(x), "#FAB860", xn1, yn1)
            xn2, yn2 = canvas.normalize_list_data(x[i], y2[i], len(x))
            xn2, yn2 = canvas.draw_function(x[i], y2[i], len(x), "#C83E4D", xn2, yn2)
        else:
            xn1, yn1 = canvas.draw_function(x[i], y1[i], len(x), "#FAB860", xn1, yn1)
            xn2, yn2 = canvas.draw_function(x[i], y2[i], len(x), "#C83E4D", xn2, yn2)
        time.sleep(0.01)
# Configuración de la ventana principal
root = tk.Tk()
root.title("Dibujo de Funciones en Canvas")
root.configure(background="#32373B")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))
root.state('zoomed')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

padx, pady = 50, 50
canvas = PlotCanvas(root)
canvas.canvas.pack(padx=padx, pady=pady)



root.update()
dibujar()
root.mainloop()
