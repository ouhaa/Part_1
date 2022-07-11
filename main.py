import tkinter as tk
from tkinter import ttk
import threading
from random import random, randint
from time import sleep

root = tk.Tk() # On crée la fenêtre.
root.title("Robots") # On lui donne un titre.
root.iconname("Robots") # On lui donne un titre.
root.resizable(False, False) # On l'empêche d'être redimensionnée.

button = tk.Button(root, text="Lancer", command=lambda: Canvas())
button.pack(side=tk.BOTTOM)
Agents = []

def createAgents(quantité, type, canvas):
    for i in range(quantité):
        position_x, position_y = randint(0, 300), randint(0, 300)
        if type == "Devil":
            canvas.create_oval(position_x, position_y, position_x+20, position_y+20, fill="yellow")


def Canvas():
    global Agents

    canvas = tk.Canvas(root, width=500, height=500, bg="grey")
    canvas.pack(side=tk.RIGHT)


    water = canvas.create_oval(300, 300, 10+50, 10+200, fill="blue")
    Agents.append(water)

    devil = canvas.create_oval(0, 0, 10, 10, fill="yellow")
    Agents.append(devil)

    thread = threading.Thread(target = MoveDevil, args = (canvas, devil))
    thread.daemon = True
    thread.start()


def MoveDevil(canvas, devil):
    sleep(2)
    canvas.move(devil, 200, 200)


  # createAgents(10, "Devil", canvas)


print(Agents)


root.mainloop() # On démarre la fenêtre.
print("Fenêtre fermée.")