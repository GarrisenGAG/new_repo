import tkinter as tk
import random

# Участник 1: Функция генерации пароля (начало)
def generate_password():
    password = ''
    try:
        length = int(entry.get())
    except ValueError:
        return
     for i in range(length):
        if random.random() > 0.5:
            password += str(random.randint(0, 9))
        else:
            if random.random() > 0.5:
                password += chr(random.randint(97,122))
            else:
                password += chr(random.randint(65, 90))
    write_pass = tk.Label(window, text = password)
    write_pass.pack()
