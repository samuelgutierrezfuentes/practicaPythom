class Producto():
    def __init__(self, id_producto, nombre, precio, peso):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__peso = peso
    
    def datosProducto(self):
        print("id producto: ", self.__id_producto)
        print("nombre: ", self.__nombre)
        print("precio: ", self.__precio)
        print("peso: ", self.__peso)
    
    def get_id_producto(self):
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

    
        