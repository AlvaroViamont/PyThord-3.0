import tkinter as tk
import tkinter.font as fnt
import random
import time
import threading

root = tk.Tk()
root.geometry('400x200+300+300')

colors = {
    "EART_YELLOW": "#FAB860",
    "ONYX": "#32373B",
    "OUTER_SPACE": "#4A5859",
    "ANTI_FLASH_WHITE": "#F0F0F0",
    "BITTERSWEET_SHIMMER": "#C83E4D",
    "CELADON_GREEN": "#2E8B57",   
    "DEEP_CARMINE_PINK": "#EF3038",
    "SMOKY_TOPAZ": "#935A5C"
}
SMALL_REGULAR_FONT = fnt.Font(family='Lato', size=12)
execute = True
frame1 = tk.Frame(root, bg=colors["ONYX"], width=200, height=20)
frame1.pack_propagate(False)  # Evita que el frame ajuste su tamaño al contenido
frame1.pack(side=tk.TOP, padx=50, pady=50, anchor='w')
max_width = 20
label1 = tk.Label(frame1, bg=colors["CELADON_GREEN"], width=max_width)
label1.pack(side=tk.LEFT, anchor='w')
var = tk.IntVar()
var.set(100)
label2 = tk.Label(frame1, bg=colors["OUTER_SPACE"], text=f'{var.get()} %', foreground=colors["ANTI_FLASH_WHITE"], font=SMALL_REGULAR_FONT, width=5)
label2.pack(side=tk.RIGHT, anchor='e')
thread:threading.Thread|None = None
direction = 1


def change_color():
    if var.get() <= 20:
        label1.config(bg=colors["DEEP_CARMINE_PINK"])
        return True
    if var.get() <= 50:
        label1.config(bg=colors["EART_YELLOW"])
        return True
    label1.config(bg=colors["CELADON_GREEN"])
    return True

def change_size():
    new_size = max_width * (var.get()/100)
    label1.config(width=int(new_size))
    label2.config(text=f'{var.get()} %')

def charged():
    global direction
    new_value = var.get() + random.randint(1, 10)*direction
    if new_value >= 0 and new_value <= 100:
        var.set(new_value)
        change_size()
        change_color()
        return True
    else:
        if direction == 1:
            direction = -1
        else:
            direction = 1
        return False

def threading_funtion():
    global execute
    while execute:
        if charged():
            time.sleep(0.5)
    return True

def start_buttom():
    global thread
    thread = threading.Thread(target=threading_funtion, daemon=True)
    thread.start()

def end():
    global execute
    execute = False
    if thread is not None and thread.is_alive():
        thread.join()
    root.destroy()


buttom1 = tk.Button(root, bg=colors["OUTER_SPACE"], fg=colors["ANTI_FLASH_WHITE"], text='iniciar', command=start_buttom, font=SMALL_REGULAR_FONT, height=2, width=10)
buttom1.pack(side=tk.TOP, padx=50, anchor='w')
root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()

