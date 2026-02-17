import tkinter as tk
class PassGenerator:
    def __init__(self, root):
        self.root = root 
        self.root.title("Генератор паролей")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        

root = tk.Tk()
app = PassGenerator(root)
root.mainloop()