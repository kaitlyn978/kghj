from tkinter import *
root=Tk()
root.title("ASCII")
root.geometry("444x444")
root.configure(background='lightblue')
enrty1=Entry(root)
enrty.place(relx=0.5,rely=0.4, anchor=CENTER)
label=Label(root,text="ASCII code is",bg="royal blue",fg="black")
def ASCIIcode():
    text_input=entry1.get()
    for letter in text_input:
        label["text"]+=str(ord(letter))
btn=Button(root,command=ASCIIcode,bg="pink",fg="black",text="show name in ASCII")
btn.place(relx=0.5,rely=0.5,anchor=CENTER);
label.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()