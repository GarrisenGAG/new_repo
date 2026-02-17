import tkinter as tk
import random

# Участник 1: Функция генерации пароля (начало)
def generate_password():
    password = ''
    try:
        length = int(entry.get())
    except ValueError:
        return