import tkinter as tk

class GameState:
    def __init__(self):
        self.piezas = [
            ["tB", "cB", "aB", "rB", "r2B", "aB", "cB", "tB"],
            ["pB", "pB", "pB", "pB", "pB", "pB", "pB", "pB"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["pN", "pN", "pN", "pN", "pN", "pN", "pN", "pN"],
            ["tN", "cN", "aN", "rN", "r2N", "aN", "cN", "tN"]
        ]

class App():
    def __init__(self, Lado_Cuadrado):
        self.gs = GameState()
        self.Lado_Cuadrado = Lado_Cuadrado
        self.imagenes = {}

        self.ventana = tk.Tk()
        self.ventana.title("Ajedrez")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.geometry(f"{str(Lado_Cuadrado * 8)}x{str(Lado_Cuadrado * 8)}")
        self.ventana.resizable(0, 0)

        self.fondo = tk.Canvas(self.ventana)
        self.fondo.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def tablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.fondo.create_rectangle(i * self.Lado_Cuadrado, j * self.Lado_Cuadrado, (i+1) * self.Lado_Cuadrado, (j+1) * self.Lado_Cuadrado, fill="#DDB88C")
                else:
                    self.fondo.create_rectangle(i * self.Lado_Cuadrado, j * self.Lado_Cuadrado, (i+1) * self.Lado_Cuadrado, (j+1) * self.Lado_Cuadrado, fill="#8B4513")

    def cargarImagenes(self):
        piezas = ["pB", "aB", "cB", "tB", "r2B", "rB", "pN", "aN", "cN", "tN", "r2N", "rN"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./imagenes/" + pieza + ".png").zoom(self.Lado_Cuadrado).subsample(70)
    
    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j != "--":
                    self.fondo.create_image(indice_j*self.Lado_Cuadrado, indice_i*self.Lado_Cuadrado, image=self.imagenes[j], anchor="nw")


ajedrez = App(70)
ajedrez.tablero()
ajedrez.cargarImagenes()
ajedrez.mostrarPiezas()
ajedrez()
