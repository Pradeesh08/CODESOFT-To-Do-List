from tkinter import *
class to_do_list():
    def __init__(self):
        self.root=Tk()
        self.root.title("To Do List")
        self.root.config(bg="light blue")
        self.root.geometry("600x475")
        self.title=Label(self.root,text="To Do List",font=("times new roman",35),bg="light blue")
        self.title.pack(pady=8)
        self.entry=Entry(self.root,width=17,font=("areial",15))
        self.entry.place(x=40,y=125)
        self.label=Label(self.root,text="Enter the task:",font=("areial",15,"bold"),bg="light blue")
        self.label.place(x=40,y=95)
        self.add_but=Button(self.root,text="Add",font=("areial",10),bg="white",padx=50,command=self.add)
        self.add_but.place(x=40,y=160)
        self.del_but=Button(self.root,text="Delete",font=("areial",10),bg="white",padx=44,command=self.delete)
        self.del_but.place(x=40,y=200)
        self.del_all_but=Button(self.root,text="Delete All",font=("areial",10),bg="white",padx=35,command=self.delete_all)
        self.del_all_but.place(x=40,y=240)
        self.exit_but=Button(self.root,text="Exit",font=("areial",10),bg="white",padx=51,command=self.root.destroy)
        self.exit_but.place(x=40,y=280)
        self.tasks=Listbox(self.root,width=20,height=10,font=("areial",20))
        self.tasks.place(x=250,y=105)

        self.root.mainloop()

    def add(self):
        self.tasks.insert(END,self.entry.get())
        self.entry.delete(0,END)
    def delete(self):
        self.tasks.delete(ANCHOR)
    def delete_all(self):
        self.tasks.delete(0,END)
    

if __name__=="__main__":
    to_do_list()
    
