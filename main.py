from tkinter import *

class basicform:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x800")
        self.root.resizable(False, False)
        self.root.title('') 
        home = homepage()
        self.root.mainloop()

class homepage:
    def __init__(self):
        self.user_name = Label(text = "Username").place(x = 40,y = 60)



if __name__ == "__main__":
    window = basicform()

  
