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

window = tk.Tk()
window.title("Генератор паролей")
window.geometry("800x500")
text = tk.Label(window, text = "Выберите длинну пароля")
text.pack()

entry = tk.Entry(window, width=15)
entry.pack(pady=10)

button = tk.Button(window, text = "Сгенерировать", command = generate_password)
button.pack()
