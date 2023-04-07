from tkinter import Tk, Button, Frame, messagebox, Label, PhotoImage, Entry, END
from tkinter.ttk import Style

# Lista de contactos de emergencia
contactos = [
    {'nombre': 'Juan Pérez', 'telefono': '4424656219'},
    {'nombre': 'María López', 'telefono': '4423234567'},
    {'nombre': 'Pedro García', 'telefono': '4427890123'}
]

# Función para mostrar los contactos en la sección 2
def mostrar_contactos():
    # Eliminamos los widgets existentes
    for widget in seccion2.grid_slaves():
        widget.destroy()
    # Creamos los labels de los contactos
    for i, contacto in enumerate(contactos):
        nombre = contacto['nombre']
        telefono = contacto['telefono']
        nombre_label = Label(seccion2, text=nombre, font=("Helvetica", 16), fg="#222", bg="#EFEFEF", padx=10, pady=5)
        telefono_label = Label(seccion2, text=telefono, font=("Helvetica", 16), fg="#222", bg="#EFEFEF", padx=10, pady=5)
        borrar_btn = Button(seccion2, text="Borrar", font=("Helvetica", 16), bg="#EFEFEF", fg="#BB0000", bd=0, command=lambda i=i: borrar_contacto(i))
        # Colocamos los widgets en la grid
        nombre_label.grid(row=i, column=0, sticky="w")
        telefono_label.grid(row=i, column=1, sticky="w")
        borrar_btn.grid(row=i, column=2, sticky="e")

# Función para añadir un nuevo contacto
def añadir_contacto():
    # Obtenemos los valores de los Entry
    nombre = nombre_entry.get()
    telefono = telefono_entry.get()
    # Verificamos que se haya ingresado un nombre y un teléfono
    if nombre == '' or telefono == '':
        messagebox.showerror('Error', 'Por favor ingresa un nombre y un teléfono')
        return
    # Agregamos el contacto a la lista
    contactos.append({'nombre': nombre, 'telefono': telefono})
    # Limpiamos los Entry
    nombre_entry.delete(0, END)
    telefono_entry.delete(0, END)
    # Mostramos los contactos actualizados
    mostrar_contactos()

# Función para borrar un contacto
def borrar_contacto(i):
    # Eliminamos el contacto de la lista
    del contactos[i]
    # Mostramos los contactos actualizados
    mostrar_contactos()

# Función para buscar un contacto
def buscar_contacto():
    # Obtenemos el valor del Entry
    query = query_entry.get().lower()
    # Buscamos el contacto en la lista
    resultados = []
    for contacto in contactos:
        if query in contacto['nombre'].lower() or query in contacto['telefono']:
            resultados.append(contacto)
    # Mostramos los resultados en la sección 2
    if len(resultados) == 0:
        messagebox.showinfo('Resultado', 'No se encontraron resultados')
    else:
        # Eliminamos los widgets existentes
        for widget in seccion2.grid_slaves():
            widget.destroy()
        # Creamos los labels de los contactos encontrados
        for i, contacto in enumerate(resultados):
            nombre = contacto['nombre']
            telefono = contacto['telefono']
            nombre_label

# Creamos la ventana principal
ventana = Tk()
ventana.title("Agenda de contactos")
ventana.config(bg="#FFFFFF")

# Creamos el título
titulo = Label(ventana, text="Agenda de contactos", font=("Arial", 30), bg="#FFFFFF")
titulo.pack(pady=10)

# Creamos la sección de agregar contactos
seccion1 = Frame(ventana, bg="#F0F0F0", pady=10)
seccion1.pack(fill="x")

nombre_label = Label(seccion1, text="Nombre:", font=("Arial", 20), bg="#F0F0F0")
nombre_label.grid(row=0, column=0, padx=10)

nombre_entry = Entry(seccion1, font=("Arial", 20))
nombre_entry.grid(row=0, column=1, padx=10)

telefono_label = Label(seccion1, text="Teléfono:", font=("Arial", 20), bg="#F0F0F0")
telefono_label.grid(row=1, column=0, padx=10)

telefono_entry = Entry(seccion1, font=("Arial", 20))
telefono_entry.grid(row=1, column=1, padx=10)

agregar_btn = Button(seccion1, text="Agregar", font=("Arial", 20), bg="#FFC000", command=añadir_contacto)
agregar_btn.grid(row=2, column=1, pady=10)

# Creamos la sección de búsqueda
seccion2 = Frame(ventana, bg="#FFFFFF", pady=10)
seccion2.pack(fill="x")

buscar_label = Label(seccion2, text="Buscar:", font=("Arial", 20), bg="#FFFFFF")
buscar_label.grid(row=0, column=0, padx=10)

query_entry = Entry(seccion2, font=("Arial", 20))
query_entry.grid(row=0, column=1, padx=10)

buscar_btn = Button(seccion2, text="Buscar", font=("Arial", 20), bg="#FFC000", command=buscar_contacto)
buscar_btn.grid(row=0, column=2, padx=10)

# Creamos la sección de contactos
seccion3 = Frame(ventana, bg="#FFFFFF", pady=10)
seccion3.pack()

mostrar_contactos()

# Iniciamos la ventana
ventana.mainloop()