from tkinter import *
fields=["Loan Amount","Number of Installments","Rate of Interest","Installments"]

def calculateInstallments(entries):
    p=float(entries[fields[0]].get())
    r=(float(entries[fields[2]].get())/100)/12
    n=float(entries[fields[1]].get())
    i=p*r*(1+r)**n/((1+r)**n-1)
    i=("%.2f"%i).strip()
    entries[fields[3]].delete(0,END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].insert(0,i)
    entries[fields[3]].config(state=DISABLED)


def makeform(root,fields):
    entries={}
    for field in fields:
        row=Frame(root)
        lab=Label(row,width=22,text=field+": ",anchor="w")
        ent=Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP,fill=X,padx=5,pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[field]=ent
    entries[field].config(state=DISABLED)
    return entries

if __name__=='__main__':
    root=Tk()
    root.title("Loan Calculator")
    ents=makeform(root,fields)
    b1=Button(root,text="Calculate Installments",command=(lambda e=ents:calculateInstallments(e)))
    b1.pack(side=LEFT,padx=5,pady=5)
    b2=Button(root,text="Exit",command=root.quit)
    b2.pack(side=LEFT,padx=5,pady=5)
    root.mainloop()
