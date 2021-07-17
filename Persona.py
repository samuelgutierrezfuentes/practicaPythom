class Persona():
    def __init__(self, nombre, movil):
        self.__nombre = nombre
        self.__movil = movil
    
    def datosPersona(self):
        print("Nombre: ", self.__nombre)
        print("Apellido: ", self.__movil)
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_movil(self):
        return self.__movil
    
    def set_movil(self, movil):
        self.__movil = movil
