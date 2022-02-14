import inspect
import tkinter as tk
from tkinter import messagebox
from collections.abc import Iterable

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


from calculator import (
    Circle,
    Rectangle,
    Square,
    Trapezoid,
    Rhombus,
    Triangle,
    Sphere,
    Parallelepiped,
    Cube,
    Cylinder,
    Cone,
    Pyramid,
    PrintResult,
)
from drawer import Drawer2D, Drawer3D


class WelcomeWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.shapes_2d = {
            "Круг": ShapeWindow(self, Circle(2), Drawer2D.draw_circle).show,
            "Прямоугольник": ShapeWindow(self, Rectangle(2, 3), Drawer2D.draw_rect).show,
            "Квадрат": ShapeWindow(self, Square(2), Drawer2D.draw_quad).show,
            "Трапеция": ShapeWindow(self, Trapezoid(8, 80, 55, 5), Drawer2D.draw_trapezoid).show,
            "Ромб": ShapeWindow(self, Rhombus(2, 4), Drawer2D.draw_rhombus).show,
            "Треугольник": ShapeWindow(self, Triangle(3, 5, 5), Drawer2D.draw_triangle).show,
        }
        self.shapes_3d = {
            "Сфера": ShapeWindow(self, Sphere(3), Drawer3D.draw_sphere).show,
            "Параллелепипед": ShapeWindow(self, Parallelepiped(2, 4, 6), Drawer3D.draw_parallelepiped).show,
            "Куб": ShapeWindow(self, Cube(2), Drawer3D.draw_cube).show,
            "Цилиндр": ShapeWindow(self, Cylinder(1, 3), Drawer3D.draw_cylinder).show,
            "Конус": ShapeWindow(self, Cone(1, 3), Drawer3D.draw_cone).show,
            "Пирамида": ShapeWindow(self, Pyramid(1, 3), Drawer3D.draw_pyramid).show,
        }

    def main_window(self):
        self.window.title("Графический калькулятор")
        self.window.resizable(False, False)
        self.create_labels()
        self.create_buttons()
        self.window.mainloop()

    def create_labels(self):
        label_2d = tk.Label(self.window, text="2D формы")
        label_3d = tk.Label(self.window, text="3D формы")
        label_2d.grid(row=0, column=0)
        label_3d.grid(row=0, column=1)

    def create_buttons(self):
        row = 1
        for shape_2d, shape_3d in zip(self.shapes_2d, self.shapes_3d):
            my_button_x = tk.Button(self.window, text=shape_2d, width=15, command=self.shapes_2d[shape_2d])
            my_button_x.grid(row=row, column=0)
            my_button_y = tk.Button(self.window, text=shape_3d, width=15, command=self.shapes_3d[shape_3d])
            my_button_y.grid(row=row, column=1)
            row += 1


class ShapeWindow:
    def __init__(self, main_window, shape, draw_method=None):
        self.main_window = main_window
        self.shape = shape
        self.draw_method = draw_method
        self.window = None
        self.fields_entries = {}

    def draw_entry(self, header, row, value):
        header = header.capitalize()
        label = tk.Label(self.window, text=f"{header}:")
        label.grid(row=row, column=0)
        entry = tk.Entry(self.window)
        entry.grid(row=row, column=1)
        entry.insert(0, PrintResult.round_result(value))
        return entry

    def draw_label(self, method, row, value):
        method = method.replace("get_", "")
        method = method.capitalize()
        if isinstance(value, Iterable):
            value = [str(PrintResult.round_result(v)) for v in value]
            value = ", ".join(value)
        else:
            value = PrintResult.round_result(value)
        label = tk.Label(self.window, text=f"{method}:")
        label.grid(row=row, column=0)
        label = tk.Label(self.window, text=f"{value}")
        label.grid(row=row, column=1)
        return label

    def show(self):
        self.window = tk.Toplevel(self.main_window.window)
        self.window.resizable(False, False)
        self.window.title("Введите параметры формы")

        fig = Figure(figsize=plt.figaspect(1), dpi=120)
        self.draw_method(fig, self.shape)
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(columnspan=2)

        row = 1
        shape_fields = inspect.signature(type(self.shape).__init__)
        shape_args = list(shape_fields.parameters.values())[1:]
        for arg in shape_args:
            value = getattr(self.shape, arg.name)
            entry = self.draw_entry(arg.name, row, value)
            self.fields_entries[arg.name] = entry
            row += 1

        shape_methods = [method for method in dir(self.shape) if method.startswith("get_")]
        for method in shape_methods:
            value = getattr(type(self.shape), method)(self.shape)
            self.draw_label(method, row, value)
            row += 1

        refresh_button = tk.Button(self.window, text="Обновить", command=self.refresh)
        refresh_button.grid(row=row + 1, column=0, columnspan=2)

    def refresh(self):
        try:
            args = []
            for field in self.fields_entries:
                new_value = float(self.fields_entries[field].get())
                args.append(new_value)
            new_shape = (type(self.shape))(*args)
            ShapeWindow(self.main_window, new_shape, self.draw_method).show()
            self.window.destroy()
        except ValueError:
            messagebox.showinfo("Произошла ошибка", "Введены некорректные данные")
