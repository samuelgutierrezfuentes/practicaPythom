from Producto import Producto


class Pedido():
    def __init__(self, idPedido):
        self.__id_pedido = idPedido
        self.__productos = []
        self.__entregado = False
    
    def agregarProducto(self, producto):
        self.__productos.append(producto)
    
    def pesoPedido(self):
        pesoTotal = 0
        for producto in self.__productos:
            pesoTotal = pesoTotal + producto.get_peso()
        
        return pesoTotal
    
    def precioPedido(self):
        total = 0
        for producto in self.__productos:
            total = total + producto.get_precio()
        
        return total
    
    def repetidos(self, id_producto):
        repeticiones = 0
        for producto in self.__productos:
            if producto.get_id_producto() == id_producto:
                repeticiones = repeticiones + 1

        return repeticiones
    
    def get_id_pedido(self):
        return self.__id_pedido
    
    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido
    
    def get_productos(self):
        return self.__productos
    
    def set_productos(self, productos):
        self.__productos = productos

    def get_entregado(self):
        return self.__entregado
    
    def set_entregado(self, entregado):
        self.__entregado = entregado

    
        
