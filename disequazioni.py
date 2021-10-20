import math
import turtle
import time
import tkinter as tk
from tkinter import messagebox
from os import system

system("title "+"Calcolatore di disequazioni")

print("Questo é un calcolatore di disequazioni di secondo grado realizzato con Python.")
a = int(float(input("Inserisci il termine a della disequazione: ")))
b = int(float(input("Inserisci il termine b della disequazione: ")))
c = int(float(input("Inserisci il termine c della disequazione: ")))

segno = input(
    "Qual é il segno della disequazione? Inserisci 'maggiore' o 'minore'. ")
if segno != "maggiore" and segno != "minore":
    print("Errore nell'inserimento dell'operatore.")
    quit()
uguale = input("Il segno ha un uguale? Scrivere 'sì' o 'no'. ")
if uguale != "sì" and uguale != "no":
    print("Errore nell'inserimento dell'uguale.")
    quit()

if segno == "maggiore":
    simbolo_segno = ">"
else:
    simbolo_segno = "<"

if uguale == "sì":
    simbolo_uguale = "="
else:
    simbolo_uguale = ""

delta = b**2-4*a*c

if delta > 0:
    deltaradice = math.sqrt(delta)
    x1 = (-b - deltaradice) / (2 * a)
    x2 = (- b + deltaradice) / (2 * a)
    x = sorted([x1, x2])
    if a > 0:
        if segno == "maggiore":
            print(
                f"Risultato: x <{simbolo_uguale} {x[0]} V x >{simbolo_uguale} {x[1]}")
        else:
            print(
                f"Risultato: {x[0]} <{simbolo_uguale} x >{simbolo_uguale} {x[1]}")
    elif a < 0:
        if segno == "maggiore":
            print(
                f"Risultato: {x[0]} <{simbolo_uguale} x >{simbolo_uguale} {x[1]}")
        else:
            print(
                f"Risultato: x <{simbolo_uguale} {x[0]} V x >{simbolo_uguale} {x[1]}")
elif delta == 0:
    x = -b / (2 * a)
    if a > 0:
        if segno == "maggiore":
            if uguale == "sì":
                print("Per ogni x appartenente a R")
            else:
                print(f"Risultato: x ≠ {x}")
        else:
            if uguale == "sì":
                print(f"Risultato: x = 0 quando x = {x}")
            else:
                print("Per nessuna x appartenente a R")
    else:
        if segno == "maggiore":
            if uguale == "sì":
                print(f"Risultato: x = 0 quando x = {x}")
            else:
                print("Per nessuna x appartenente a R")
        else:
            if uguale == "sì":
                print("Per ogni x appartenente a R")
            else:
                print(f"Risultato: x ≠ {x}")
elif delta < 0:
    if a > 0:
        if segno == "maggiore":
            print("Per nessuna x appartenente a R")
        else:
            print("Per nessuna x appartenente a R")
    else:
        if segno == "maggiore":
            print("Per nessuna x appartenente a R")
        else:
            print("Per ogni x appartenente a R")

time.sleep(3)

popup = tk.messagebox.askquestion(
    "Disegno della parabola", "Vuoi disegnare la parabola?")

if popup == "yes":
    turtle.setup(1000, 1000)
    canvas = turtle.getscreen()
    canvas.title("Disegno della parabola")
    print(canvas)
    disegno = turtle.Turtle()
    disegno.ht()
    disegno.up()
    disegno.home()
    disegno.down()
    disegno.goto(0, 500)
    disegno.goto(0, -500)
    disegno.home()
    disegno.goto(500, 0)
    disegno.goto(-500, 0)
    disegno.up()
    # Disegno del piano cartesiano
else:
    quit()

turtle.mainloop()
