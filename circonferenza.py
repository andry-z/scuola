import math
import tkinter as tk
from tkinter import messagebox
from os import system

system("title "+"Programma sulla circonferenza")

ax = float(input("Inserire la coordinata x del punto A: "))
ay = float(input("Inserire la coordinata y del punto A: "))
bx = float(input("Inserire la coordinata x del punto B: "))
by = float(input("Inserire la coordinata y del punto B: "))
cx = float(input("Inserire la coordinata x del punto C: "))
cy = float(input("Inserire la coordinata y del punto C: "))

if (ax == bx and bx == cx) or (ay == by and by == cy):
    print("ERRORE: i punti sono allineati. Il programma sarà terminato.")
    exit(1)

pm_ab = {"x": (ax + bx)/2, "y": (ay + by)/2}
m1 = (ay-by)/(ax-bx)
m_perp1 = -1/m1
q1 = pm_ab["y"] - (m_perp1 * pm_ab["x"])
pm_ac = {"x": (ax + cx)/2, "y": (ay + cy)/2}
m2 = (ay-cy)/(ax-cx)
m_perp2 = -1/m2
q2 = pm_ac["y"] - (m_perp2 * pm_ac["x"])
o = {"x": (q2-q1)/(m_perp1-m_perp2), "y": m_perp1 *
     (q2-q1)/(m_perp1-m_perp2) + q1}
r = math.sqrt((ax-o["x"])**2+(ay-o["y"])**2)

risultato = f"Centro della circonferenza: O({o['x']}; {o['y']}). \nLunghezza del raggio: {r}"
box = tk.messagebox.showinfo("Risultato", risultato)

print(f"Centro della circonferenza: O({o['x']}; {o['y']})")
print(f"Lunghezza del raggio: {r}")
