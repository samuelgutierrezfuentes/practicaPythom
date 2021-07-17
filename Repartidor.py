from Persona import Persona 

class Repartidor(Persona):
    def __init__(self, nombre, movil,  salario):
        super().__init__(nombre, movil)
        self.__salario = salario
        self.__pedidos = []

    def agregarPedido(self, pedido):
       self.__pedidos.append(pedido)

    def pesoTotal(self):
        pesoTotal = 0
        for pedido in self.__pedidos:
            pesoTotal = pesoTotal + pedido.pesoPedido()
        
        return pesoTotal
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario

    def get_pedidos(self):
        return self.__pedidos
    
    def set_pedidos(self, pedidos):
        self.__pedidos = pedidos
