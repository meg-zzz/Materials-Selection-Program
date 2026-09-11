#Import tkinter and ttk for modern-looking user interface
import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("Materials Selection Program")
main.geometry("600x800")

style = ttk.Style()
style.theme_use('classic')

main.mainloop()
