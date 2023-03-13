from tkinter import Tk, Button, Frame, messagebox, Label, Entry, PhotoImage

#1.- instanciamos el objeto ventana
ventana2= Tk()
ventana2.title("B-AX")
ventana2.geometry("1000x600")
img= PhotoImage(file="3.png")
#2.- agregamos los frame
seccion4= Frame(ventana2, bg="#18295B")
foto=Label(seccion4, image=img, height=130, width=210)
foto.place(x=0, y=0)
seccion4.pack(expand=True,fill='both')

seccion5= Frame(ventana2, bg="#B0B0B0")
seccion5.pack(expand=True,fill='both')

seccion6= Frame(ventana2, bg="#18295B")
seccion6.pack(expand=True,fill='both')

#seccion 1
titulo2= Label(seccion4,text="CONFIGURACION DE", font=("Berlin Sans FB Demi",20),fg="white", bg="#18295B")
titulo2.pack()

titulo3= Label(seccion4,text="CONTACTOS DE EMERGENCIA", font=("Berlin Sans FB Demi",20),fg="white", bg="#18295B")
titulo3.pack()

flecha2= Button(seccion4,text="<---", font=("Berlin Sans FB Demi",20), bg="#727272")
flecha2.place(x=900, y=20)

#seccion 2

gnombre= Label(seccion5,text="Nombre", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
gnombre.place(x=225, y=40)

gnumero= Label(seccion5,text="Numero", font=("Berlin Sans FB Demi",20), bg="#B0B0B0")
gnumero.place(x=700, y=40)

bnombre= Entry(seccion5, font=("Berlin Sans FB Demi",20), bg="#B0B0B0",width=15)
bnombre.place(x=150, y=90)

bnumero= Entry(seccion5, font=("Berlin Sans FB Demi",20), bg="#B0B0B0",width=15)
bnumero.place(x=625, y=90)



#seccion tres

guardar= Button(seccion6,text="Guardar", font=("Berlin Sans FB Demi",20), bg="#727272")
guardar.place(x=40, y=35)

cancelar= Button(seccion6,text="Cancelar", font=("Berlin Sans FB Demi",20), bg="#727272")
cancelar.place(x=800, y=35)

#llamamos al main (sin esto no imprime la ventana)
ventana2.mainloop()