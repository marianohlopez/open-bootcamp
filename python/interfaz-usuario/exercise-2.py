import tkinter as tk

root = tk.Tk()
root.title("Interfaz sencilla")


# Agregar elementos a la lista
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
lista_elementos = tk.StringVar(value=elementos)
# Crear la lista de elementos seleccionables
listbox = tk.Listbox(root, height=10, listvariable=lista_elementos)
listbox.pack()

# Crear el label con el texto fijo
label = tk.Label(root, text="¡Texto fijo!")
label.pack()

root.mainloop()
