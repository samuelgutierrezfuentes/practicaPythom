class Direccion():
    def __init__(self, calle, numero, piso, letra, CP, ciudad):
        self.__calle = calle
        self.__numero = numero
        self.__piso = piso
        self.__letra = letra
        self.__CP = CP
        self.__ciudad = ciudad

    def get_calle(self):
        return self.__calle
    
    def set_calle(self, calle):
        self.__calle = calle

    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero
    
    def get_piso(self):
        return self.__piso
    
    def set_piso(self, piso):
        self.__piso = piso
    
    def get_letra(self):
        return self.__letra
    
    def set_letra(self, letra):
        self.__letra = letra
    
    def get_CP(self):
        return self.__CP
    
    def set_CP(self, CP):
        self.__CP = CP
    
    def get_ciudad(self):
        return self.__ciudad
    
    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad