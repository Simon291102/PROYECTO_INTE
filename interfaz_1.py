from tkinter import Tk, Button, Frame, messagebox, Label, PhotoImage

nombre="Mateo Alejandro"
numero="4424656219"


#1.- instanciamos el objeto ventana
ventana= Tk()
ventana.title("B-AX")
ventana.geometry("1000x600")
img= PhotoImage(file="3.png")
#2.- agregamos los frame
seccion1= Frame(ventana, bg="#18295B")
foto=Label(seccion1, image=img, height=130, width=210)
foto.place(x=0, y=0)
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana, bg="#B0B0B0")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana, bg="#18295B")
seccion3.pack(expand=True,fill='both')


#seccion 1

titulo= Label(seccion1,text="CONFIGURACION DE", font=("Berlin Sans FB Demi",20),fg="white", bg="#18295B")
titulo.pack()

titulo1= Label(seccion1,text="CONTACTOS DE EMERGENCIA", font=("Berlin Sans FB Demi",20),fg="white", bg="#18295B")
titulo1.pack()

flecha= Button(seccion1,text="<---", font=("Berlin Sans FB Demi",20), bg="#727272")
flecha.place(x=900, y=20)

#seccion dos

usuario= Button(seccion2,text= nombre + "                   " + numero, font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
usuario.grid(row= 1, column= 1)

borrar= Button(seccion2,text= "Borrar", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
borrar.grid(row= 1, column= 2)

#seccion tres

añadir= Button(seccion3,text="Añadir", font=("Berlin Sans FB Demi",20), bg="#727272")
añadir.place(x=40, y=35)

borrar_todo= Button(seccion3,text="Borrar Todo", font=("Berlin Sans FB Demi",20), bg="#727272")
borrar_todo.place(x=800, y=35)

#llamamos al main (sin esto no imprime la ventana)
ventana.mainloop()