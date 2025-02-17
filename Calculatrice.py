import tkinter as tk

calcul=""

def ajout_calcul(symbol):
    global calcul
    calcul += str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)

def eval_calcul():
    global calcul
    try:
        calcul =str(eval(calcul))
        text_resultat.delete(1.0,"end")
        text_resultat.insert(1.0,calcul)
    
    except:
        effacer_ecran()
        text_resultat.insert(1.0,"Erreur")

def effacer_ecran():
    global calcul
    calcul = ""
    text_resultat.delete(1.0,"end")

root=tk.Tk()
root.title("Calculatrice")
root.geometry("300x275")
root.iconbitmap("calculator.ico")
text_resultat=tk.Text(root,height=2,width=116)
text_resultat.grid(columnspan=5)
btn_1=tk.Button(root,text="1",command= lambda:ajout_calcul(1),width = 5, font=('Arial'))
btn_1.grid(row=2, column= 1)
btn_2=tk.Button(root,text="2",command= lambda:ajout_calcul(2),width = 5, font=('Arial'))
btn_2.grid(row=2, column= 2)
btn_3=tk.Button(root,text="3",command= lambda:ajout_calcul(3),width = 5, font=('Arial'))
btn_3.grid(row=2, column= 3)
#étage 3 

btn_4=tk.Button(root,text="4",command= lambda:ajout_calcul(4),width = 5, font=('Arial'))
btn_4.grid(row=3, column= 1)
btn_5=tk.Button(root,text="5",command= lambda:ajout_calcul(5),width = 5, font=('Arial'))
btn_5.grid(row=3, column= 2)
btn_6=tk.Button(root,text="6",command= lambda:ajout_calcul(6),width = 5, font=('Arial'))
btn_6.grid(row=3, column= 3)

#etage 4

btn_7=tk.Button(root,text="7",command= lambda:ajout_calcul(7),width = 5, font=('Arial'))
btn_7.grid(row=4, column= 1)
btn_8=tk.Button(root,text="8",command= lambda:ajout_calcul(8),width = 5, font=('Arial'))
btn_8.grid(row=4, column= 2)
btn_9=tk.Button(root,text="9",command= lambda:ajout_calcul(9),width = 5, font=('Arial'))
btn_9.grid(row=4, column= 3)
#dernier étage 

btn_0=tk.Button(root,text="0",command= lambda:ajout_calcul(0),width = 5, font=('Arial'))
btn_0.grid(row=5, column= 2)

btn_pg=tk.Button(root,text="(",command= lambda:ajout_calcul("("),width = 5, font=('Arial'))
btn_pg.grid(row=5, column= 1)
btn_pd=tk.Button(root,text=")",command= lambda:ajout_calcul(")"),width = 5, font=('Arial'))
btn_pd.grid(row=5, column= 3)


btn_plus=tk.Button(root,text="+",command= lambda:ajout_calcul("+"),width = 5, font=('Arial'))
btn_plus.grid(row=2, column= 4)
btn_sous=tk.Button(root,text="-",command= lambda:ajout_calcul("-"),width = 5, font=('Arial'))
btn_sous.grid(row=3, column= 4)
btn_fois=tk.Button(root,text="*",command= lambda:ajout_calcul("*"),width = 5, font=('Arial'))
btn_fois.grid(row=4, column= 4)
btn_div=tk.Button(root,text="/",command= lambda:ajout_calcul("/"),width = 5, font=('Arial'))
btn_div.grid(row=5, column= 4)


btn_egal=tk.Button(root,text="=",command= eval_calcul,width = 5, font=('Arial'))
btn_egal.grid(row=6, column= 2)
btn_del=tk.Button(root,text="C",command=effacer_ecran,width = 5, font=('Arial'))
btn_del.grid(row=6, column= 3)

root.mainloop()