from tkinter import Tk, Button, Frame, messagebox, Label

nombre="Mateo Alejandro"
numero="4424656219"

#1.- instanciamos el objeto ventana
ventana= Tk()
ventana.title("B-AX")
ventana.geometry("600x400")

#2.- agregamos los frame
seccion1= Frame(ventana, bg="#727272")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana, bg="#B0B0B0")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="#727272")
seccion3.pack(expand=True,fill='both')


#seccion 1
titulo= Label(seccion1,text="CONFIGURACION DE", font=("Berlin Sans FB Demi",20), bg="#727272")
titulo.place(x=30, y=1)

titulo1= Label(seccion1,text="CONTACTOS DE EMERGENCIA", font=("Berlin Sans FB Demi",20), bg="#727272")
titulo1.place(x=30, y=40)

flecha= Button(seccion1,text="<---", font=("Berlin Sans FB Demi",20), bg="#727272")
flecha.place(x=500, y=20)

#seccion dos

usuario= Button(seccion2,text= nombre + "                   " + numero, font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
usuario.grid(row= 1, column= 1)

borrar= Button(seccion2,text= "Borrar", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
borrar.grid(row= 1, column= 2)

#seccion tres

añadir= Button(seccion3,text="Añadir", font=("Berlin Sans FB Demi",20), bg="#727272")
añadir.place(x=60, y=35)

borrar_todo= Button(seccion3,text="Borrar Todo", font=("Berlin Sans FB Demi",20), bg="#727272")
borrar_todo.place(x=400, y=35)

#llamamos al main (sin esto no imprime la ventana)
ventana.mainloop()