print("Programacion POO")
# definicion de clases
class Perro:
    
# Funciones dentro de laa clase
    edad=4
    def morder(self):
        print("El perro me mordio")
    def datosperro (self,nombre,edad):
        print(f"Nombre: {nombre} edad : {edad}")
    
# zona de creacion de objeto
pitbull=Perro()

# zona de uso de objetos
pitbull.datosperro("lasky",4)
pitbull.morder()