import tkinter as tk


def reset_selection():
    # Deseleccionar todas las opciones
    for button in radio_buttons:
        button.deselect()
    # Actualizar el label con la opción seleccionada
    selected_option.set("Ninguna opción seleccionada")


root = tk.Tk()
root.title("RadioButtons Example")

selected_option = tk.StringVar()
selected_option.set("Ninguna opción seleccionada")

radio_buttons = []

# Crear los RadioButtons
option1 = tk.Radiobutton(
    root,
    text="Opción 1",
    variable=selected_option,
    value="Opción 1",
)
option1.pack()
radio_buttons.append(option1)

option2 = tk.Radiobutton(
    root,
    text="Opción 2",
    variable=selected_option,
    value="Opción 2",
)
option2.pack()
radio_buttons.append(option2)

option3 = tk.Radiobutton(
    root,
    text="Opción 3",
    variable=selected_option,
    value="Opción 3",
)
option3.pack()
radio_buttons.append(option3)

# Crear el botón de reinicio
reset_button = tk.Button(root, text="Reiniciar", command=reset_selection)
reset_button.pack()

# Crear el label para mostrar la opción seleccionada
selection_label = tk.Label(root, textvariable=selected_option)
selection_label.pack()

root.mainloop()
