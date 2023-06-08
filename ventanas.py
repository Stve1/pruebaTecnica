import tkinter as tk
from tkinter import messagebox
from tkinter import*

pant = tk.Tk()
pant.title("To Do List")
pant.geometry("300x600")
pant.resizable(0,0)
pant.iconbitmap('form.ico')

tareasL = tk.Listbox(pant)
i = 0
x = 0
tk.Label(pant, text="   ¡Bienvenido a tu lista de tareas!   \n").pack()

logo = tk.PhotoImage(file="SunD.png")
imagen = tk.Label(pant, image=logo, width=150, height=150).pack()

def inTareas():
    entrada = campo.get()
    tareasL.insert(0, entrada)
            
def busTareas():
    entrada = campo.get()
    items = tareasL.get(0, END)
    texExito = "La tarea sí se encuentra registrada en la posición {}"
    for x, tarea in enumerate(items):
        if tarea == entrada:
            messagebox.showinfo("Búsqueda exitosa.", texExito.format(x+1))
        else:
            messagebox.showinfo("No encontrado.", "La tarea no se encuentra en la lista.")
        return

def elimTareas():
    sel = tareasL.curselection()
    tareasL.delete(sel)
    
campo = tk.Entry()
campo.pack()
botIngrTareas = tk.Button(pant, text="Ingresar una nueva tarea.", command=inTareas, width=25).pack()
botBuscarTareas = tk.Button(pant, text="Buscar una tarea en la lista.",command=busTareas, width=25).pack()
botElimTareas = tk.Button(pant, text="Eliminar una tarea.",command=elimTareas, width=25).pack()
botCerrar = tk.Button(pant, text="Salir", command=lambda: pant.destroy(), width=25).pack()

tareasL.place(x=90,y= 350)

pant.mainloop()