import math
import tkinter as tk
from tkinter import messagebox

a = float(input("Inserisci la lunghezza del lato A: "))
b = float(input("Inserisci la lunghezza del lato B: "))
c = float(input("Inserisci la lunghezza del lato C: "))
p = (a + b + c)/2
area = math.sqrt((p*(p - a)*(p - b)*(p - c)))

r_inscritta = (2 * area) / (a + b + c)
r_circoscritta = (a * b * c) / (4 * area)

risultato = f"Raggio della circonferenza inscritta: {r_inscritta}. \nRaggio della circonferenza circoscritta: {r_circoscritta}."

box = tk.messagebox.showinfo("Risultato", risultato)

print(risultato)

numeri = [a, b, c]
numeri.sort()

if numeri[0] < numeri[2] - numeri[1] or numeri[2] > numeri[0] + numeri[1]:
    print("I lati non formano un triangolo.")
    quit()
