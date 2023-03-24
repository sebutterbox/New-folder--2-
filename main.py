import tkinter as tk

class basicform:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x450")
        self.root.resizable(False, False) 
        self.root.mainloop()
  
if __name__ == "__main__":
    window = basicform()

  
