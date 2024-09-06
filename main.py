class Cuadrado:
    def __init__(self, tamaño):
        self.tamaño = tamaño

    def dibujar(self):
        for _ in range(self.tamaño):
            print('*' * self.tamaño)

# Solicitar el tamaño del cuadrado al usuario
tamaño = int(input("Introduce el tamaño del cuadrado: "))

# Crear una instancia de la clase Cuadrado
cuadrado = Cuadrado(tamaño)

# Dibujar el cuadrado
cuadrado.dibujar()
