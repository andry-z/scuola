import math
import tkinter as tk
from tkinter import messagebox
from os import system

system("title "+"Risolutore di triangoli")

caso = input("""Inserisci la lettera corrispondente ai dati di cui sei in possesso:
a) Due cateti
b) Un cateto e l'ipotenusa
c) Due proiezioni
d) Altezza relativa all'ipotenusa e una proiezione
e) Altezza relativa all' ipotenusa e ipotenusa
f) Altezza relativa all'ipotenusa e un cateto
g) Un cateto e la sua proiezione
Triangolo 30° - 60° - 90°
    h) Ipotenusa
    i) Cateto opposto all'angolo di 30°
    l) Cateto opposto all'angolo di 60°
Triangolo 45° - 45° - 90°
    m) Ipotenusa
    n) Cateto
""")

if caso != "a" and caso != "b" and caso != "c" and caso != "d" and caso != "e" and caso != "f" and caso != "g" and caso != "h" and caso != "i" and caso != "l" and caso != "m" and caso != "n":
    print("Inserire una lettera tra a-n.")
    quit()

if caso == "a":
    cateto1 = float(input("Inserire cateto 1: "))
    cateto2 = float(input("Inserire cateto 2: "))
    ipotenusa = math.sqrt(cateto1**2 + cateto2**2)
elif caso == "b":
    ipotenusa = float(input("Inserire ipotenusa: "))
    cateto1 = float(input("Inserire cateto 1: "))
    cateto2 = math.sqrt(ipotenusa**2 - cateto1**2)
elif caso == "c":
    proiezione1 = float(input("Inserire proiezione 1: "))
    proiezione2 = float(input("Inserire proiezione 2: "))
    ipotenusa = proiezione1 + proiezione2
    altezza_ipotenusa = math.sqrt(proiezione1 * proiezione2)
    cateto1 = math.sqrt(altezza_ipotenusa**2 + proiezione1**2)
    cateto2 = math.sqrt(altezza_ipotenusa**2 + proiezione2**2)
elif caso == "d":
    altezza = float(input("Inserire altezza: "))
    proiezione1 = float(input("Inserire proiezione 1: "))
    cateto1 = math.sqrt(altezza**2 + proiezione1**2)
    ipotenusa = cateto1**2/proiezione1
    proiezione2 = altezza**2/proiezione1
    cateto2 = math.sqrt(altezza**2+proiezione2**2)
elif caso == "e":
    altezza = float(input("Inserire altezza: "))
    ipotenusa = float(input("Inserire ipotenusa: "))

    proiezione1 = (ipotenusa-math.sqrt(ipotenusa**2-4 * altezza**2))/2
    if proiezione1 > 0 and ((ipotenusa - proiezione1) > 0):
        print(f"Proiezione 1: {proiezione1}")
        proiezione2 = ipotenusa - proiezione1
        cateto1 = math.sqrt(altezza**2 + proiezione1**2)
        cateto2 = math.sqrt(altezza**2+proiezione2**2)
        print(f"Proiezione 2: {proiezione2}")
        print(f"Cateto 1: {cateto1}")
        print(f"Cateto 2: {cateto2}")
        p = cateto1 + cateto2 + ipotenusa
        print(f"Perimetro: #{p}")
        a = (cateto1 * cateto2) / 2
        print(f"Area: #{a}")
    else:
        print("Trovata una soluzione non accettabile")

    proiezione1 = (ipotenusa+math.sqrt(ipotenusa**2-4 * altezza**2))/2
    if proiezione1 > 0 and ((ipotenusa - proiezione1) > 0):
        print(f"Proiezione 1: {proiezione1}")
        proiezione2 = ipotenusa - proiezione1
        cateto1 = math.sqrt(altezza**2 + proiezione1**2)
        cateto2 = math.sqrt(altezza**2+proiezione2**2)
        print(f"Proiezione 2: {proiezione2}")
        print(f"Cateto 1: {cateto1}")
        print(f"Cateto 2: {cateto2}")
        p = cateto1 + cateto2 + ipotenusa
        print(f"Perimetro: #{p}")
        a = (cateto1 * cateto2) / 2
        print(f"Area: #{a}")
    else:
        print("Trovata una soluzione non accettabile")
    exit(1)
elif caso == "f":
    altezza = float(input("Inserire altezza: "))
    cateto1 = float(input("Inserire cateto1: "))
    proiezione1 = math.sqrt(cateto1**2-altezza**2)
    ipotenusa = cateto1**2/proiezione1
    proiezione2 = altezza**2/proiezione1
    cateto2 = math.sqrt(altezza**2+proiezione2**2)
elif caso == "g":
    cateto1 = float(input("Inserire cateto 1: "))
    proiezione1 = float(input("Inserire proiezione 1: "))
    altezza = math.sqrt(cateto1**2-proiezione1**2)
    ipotenusa = cateto1**2/proiezione1
    proiezione2 = altezza**2/proiezione1
    cateto2 = math.sqrt(altezza**2+proiezione2**2)
elif caso == "h":
    ipotenusa = float(input("Inserire ipotenusa: "))
    cateto1 = ipotenusa / 2
    cateto2 = (ipotenusa / 2) * math.sqrt(3)
elif caso == "i":
    cateto1 = float(
        input("Inserire il cateto minore (opposto all'angolo di 30º): "))
    ipotenusa = 2 * cateto1
    cateto2 = (ipotenusa/2) * math.sqrt(3)
elif caso == "l":
    cateto2 = float(
        input("Inserire il cateto maggiore (opposto all'angolo di 60º): "))
    ipotenusa = (2*cateto2) / math.sqrt(3)
    cateto1 = ipotenusa / 2
elif caso == "m":
    ipotenusa = float(input("Inserire l'ipotenusa: "))
    cateto1 = ipotenusa / math.sqrt(2)
    cateto2 = cateto1
elif caso == "n":
    cateto1 = float(input("Inserire il cateto: "))
    cateto2 = cateto1
    ipotenusa = cateto1 * math.sqrt(2)

area = (cateto1 * cateto2) / 2
perimetro = cateto1 + cateto2 + ipotenusa
print(f"Cateto 1: {cateto1}")
print(f"Cateto 2: {cateto2}")
print(f"Ipotenusa: {ipotenusa}")
print(f"Perimetro: {perimetro}")
print(f"Area: {area}")

risultato_cateto1 = f"Il cateto 1 é {cateto1}, il cateto 2 é {cateto2}, l'ipotenusa é {ipotenusa}, il perimetro é {perimetro} e l'area é {area}."

popup = tk.messagebox.showinfo(
    "Risultato", risultato_cateto1)
