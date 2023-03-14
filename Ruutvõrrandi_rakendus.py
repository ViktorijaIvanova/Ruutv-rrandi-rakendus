from msvcrt import kbhit
from tkinter import* #графика

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)
tekst="Aken"
aken=Tk() #открытик графическоого окна
aken.geometry("500x700") #размер окна
aken.title(tekst) #название окна 

pealkiri=Label(aken,text="Решение квадратного уравнения",
               bg="Lightblue",
               fg="green",
               font="Algerian 20",
               height=3,
               width=30) #оформление текста,окна
nupp=Button(aken,
            text="Решить",
            bg="Green",
            fg="black",
            font="Algerian 20",
            activebackground="Green",
            activeforeground="black",
            height=3,
            width=10,
            justify=RIGHT) #делаем кнопку
st_kast=Entry(aken,
                 fg="black",
                 bg="lightblue",
                 font="Algerian 20",
                 width=4,
                 justify=LEFT)
ekst_kast=Entry(aken,
                 fg="black",
                 bg="lightblue",
                 font="Algerian 20",
                 width=4,
                 justify=CENTER)
kst_kast=Entry(aken,
                 fg="black",
                 bg="lightblue",
                 font="Algerian 20",
                 width=4,
                 justify=RIGHT)


tekst_kast=Label(aken,text="Решить",
                 fg="black",
                 bg="yellow",
                 font="Algerian 20",
                 width=20,
                 justify=CENTER)
tekst_kast.bind("<Return>",text_to_lbl)#bind делает связь между элементами
pealkiri.pack() #упаковка элементов

nupp.pack()
st_kast.pack()
ekst_kast.pack()
kst_kast.pack()
tekst_kast.pack() #side=LEFT,RIGHT
aken.mainloop() #отобразить окно
