from tkinter import Tk, Button, Frame, messagebox, Label, Entry

#1.- instanciamos el objeto ventana
ventana2= Tk()
ventana2.title("B-AX")
ventana2.geometry("600x400")

#2.- agregamos los frame
seccion4= Frame(ventana2, bg="#727272")
seccion4.pack(expand=True,fill='both')

seccion5= Frame(ventana2, bg="#B0B0B0")
seccion5.pack(expand=True,fill='both')

seccion6= Frame(ventana2, bg="#727272")
seccion6.pack(expand=True,fill='both')

#seccion 1
titulov2= Label(seccion4,text="CONFIGURACION DE", font=("Berlin Sans FB Demi",20), bg="#727272")
titulov2.place(x=30, y=1)

titulo1v2= Label(seccion4,text="CONTACTOS DE EMERGENCIA", font=("Berlin Sans FB Demi",20), bg="#727272")
titulo1v2.place(x=30, y=40)

flecha= Button(seccion4,text="<---", font=("Berlin Sans FB Demi",20), bg="#727272")
flecha.place(x=500, y=20)

#seccion 2

gnombre= Label(seccion5,text="Nombre", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
gnombre.place(x=75, y=1)

gnumero= Label(seccion5,text="Numero", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
gnumero.place(x=410, y=1)

bnombre= Entry(seccion5, font=("Berlin Sans FB Demi",20), bg="#B0B0B0",width=15)
bnombre.place(x=20, y=50)

bnumero= Entry(seccion5, font=("Berlin Sans FB Demi",20), bg="#B0B0B0",width=15)
bnumero.place(x=325, y=50)



#seccion tres

añadir= Button(seccion6,text="Guardar", font=("Berlin Sans FB Demi",20), bg="#727272")
añadir.place(x=60, y=35)

borrar_todo= Button(seccion6,text="Cancelar", font=("Berlin Sans FB Demi",20), bg="#727272")
borrar_todo.place(x=400, y=35)

#llamamos al main (sin esto no imprime la ventana)
ventana2.mainloop()