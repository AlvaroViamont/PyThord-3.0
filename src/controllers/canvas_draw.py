from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

plt.style.use('seaborn-v0_8-dark')  # Usar un estilo base que armonice con los colores

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

custom_style = {
    "axes.facecolor": colors["OUTER_SPACE"],
    "axes.edgecolor": colors["ONYX"],
    "axes.labelcolor": colors["ANTI_FLASH_WHITE"],
    "xtick.color": colors["EART_YELLOW"],
    "ytick.color": colors["EART_YELLOW"],
    "text.color": colors["ANTI_FLASH_WHITE"],
    "figure.facecolor": colors["ONYX"],
    "figure.edgecolor": colors["ONYX"],
    "grid.color": colors["CELADON_GREEN"],
    "lines.linewidth": 2.5,
    "lines.color": colors["BITTERSWEET_SHIMMER"],
    "patch.edgecolor": colors["DEEP_CARMINE_PINK"],
    "patch.facecolor": colors["BITTERSWEET_SHIMMER"],
    "axes.prop_cycle": plt.cycler('color', [
        colors["EART_YELLOW"],
        colors["BITTERSWEET_SHIMMER"],
        colors["CELADON_GREEN"],
        colors["DEEP_CARMINE_PINK"],
        colors["ANTI_FLASH_WHITE"]
    ])
}

plt.rcParams.update(custom_style)


class PlotFrame():
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.min = -60
        self.max = 60

    def plot_data(self, x_data, y_data, label):
        self.ax.plot(x_data, y_data, label=label)
        plt.ylim(self.min, self.max)
        plt.xlabel('Tiempo (ms)')
        plt.ylabel('Angulo (grados)')
        y_min, y_max = plt.ylim()
        y_ticks = np.arange(y_min, y_max + 20, 20)
        plt.yticks(y_ticks)
    
    def plot_data_mark (self, x_data, y_data, label):
        self.ax.scatter(x_data, y_data, label=label, marker='o', color='#F0F0F0', s=60)
        plt.ylim(self.min, self.max)
        plt.xlabel('Tiempo (ms)')
        plt.ylabel('Angulo (grados)')
        y_min, y_max = plt.ylim()
        y_ticks = np.arange(y_min, y_max + 20, 20)
        plt.yticks(y_ticks)
    
    def destroy_plot(self):
        """Método para destruir el canvas y liberar recursos cuando no sea necesario."""
        self.canvas.get_tk_widget().destroy()
        plt.close(self.fig)



class PlotCanvas:
    def __init__(self, parent:tk.Frame):
        self.width = 800
        self.height = 500
        self.canvas = tk.Canvas(parent, width=self.width, height=self.height, bg=colors['OUTER_SPACE'])
    
    def normalize_list_data(self, x, y, xzise):
        width = self.canvas.winfo_width()/4
        height = self.canvas.winfo_height()
        x_normalized = ((width-70)-70)*((x-1)/xzise-1)+70
        y_normalized = height - 70 - ((height - 70) - 70)*((y - (-60))/(60-(-60)))
        return x_normalized, y_normalized
    
    def draw_axes(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        self.canvas.create_rectangle(20, 20, width-20, height-20, fill=colors['ONYX'])
        self.canvas.create_line(50, 50, 50, height-50, fill=colors['ANTI_FLASH_WHITE'], width=2)
        self.canvas.create_line(50, height-50, width-50, height-50, fill=colors['ANTI_FLASH_WHITE'], width=2)
        
    def draw_grid(self, step=50):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        for y in range(0, height, step):
            self.canvas.create_line(0, y, width, y, fill=colors['CELADON_GREEN'], dash=(4, 2))
        for x in range(0, width, step):
            self.canvas.create_line(x, 0, x, height, fill=colors['CELADON_GREEN'], dash=(4, 2))
    
    def draw_function(self, x, y, xzise, color, xn, yn):
        timelist, points1 = self.normalize_list_data(x, y, xzise)
        xd1, yd1 = xn, yn
        xd2, yd2 = timelist, points1
        self.canvas.create_line(xd1, yd1, xd2, yd2, fill=color, width=2)
        self.canvas.update()
        return xd2, yd2