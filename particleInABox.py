import plotly.graph_objects as go
import numpy as np
import PySimpleGUI as sg

# Długość boków pudełka
L = 1
# Generowanie wartości dla poszczególnych zmiennych
X, Y, Z = np.mgrid[0:L:0.03, 0:L:0.03, 0:L:0.03]
# Stała będąca rozwiązaniem równania Schrödingera
A = (2/L)**(1/2)

# Wzór określający prawdopodobieństwo położenia cząstki w pudełku
def fun_prawd (X, Y, Z, n):
    return np.abs(A**(3/2) * ( np.sin(n * np.pi * X / L) *
                            np.sin(n * np.pi * Y / L) * np.sin(n * np.pi * Z / L) ))**2

# Funkcja generująca wykres w zależności od liczby kwantowej
def gen_wykres (n):

    values = fun_prawd(X,Y,Z, n)

    fig = go.Figure(data=go.Volume(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value = values.flatten(),
        isomin=0.1,
        isomax=0.8,
        opacity=0.1, 
        surface_count=20, 
        ))
    fig.update_layout(title = "Prawdopodobieństwo położenia cząstki w pudełku", 
                      title_x=0.5, 
                      title_font=dict(size=30, family='Arial, sans-serif'))
    fig.show()


# Proste GUI (lepsze niż wpisywanie wartości z palca)
sg.theme("SandyBeach")
layout = [[sg.Text("Wybierz liczbę kwantową.", size=(20,1), font="Lucida", justification="left")], 
          [sg.Combo([1,2,3], default_value=1, key="number", size=10)],
          [sg.Button("Wygeneruj wykres prawdopodobieństwa", size=30)],
          [sg.Button("Zamknij program", size=30)]]
window = sg.Window(title = "Cząstka w pudełku 3D", layout=layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event is None or event == "Zamknij program":               
        break
    if event == "Wygeneruj wykres prawdopodobieństwa.":
        gen_wykres (values["number"])
window.close()

