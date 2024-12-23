from  tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Cozyfit | Developed by Devashish Das")
        self.root.config(bg="white")
        self.root.focus_force()
        #=================================




if __name__=="__main__":
    root = Tk()
    ims = productClass(root)
    root.mainloop()
