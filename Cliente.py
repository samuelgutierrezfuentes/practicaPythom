from Persona import Persona 
import re

class Cliente(Persona):
    def __init__(self, nombre, movil,  direccion):
        super().__init__(nombre, movil)
        self.__email = ''
        self.__direccion = direccion
        self.__pedidos = []
    
    def agregarPedido(self, pedido):
        #Validar si existe el idPedido
        existePedido = False 
        for pedido_ in self.__pedidos:
            if pedido_.get_id_pedido() == pedido.get_id_pedido():
                existePedido = True
        
        #si no existe procedemos a agregar el pedido
        if existePedido == False:
            self.__pedidos.append(pedido)

    def pedidosEntregados(self):
        pedidosEntregados_ =[]
        for pedido_ in self.__pedidos:
            if pedido_.get_entregado() == True:
                pedidosEntregados_.append(pedido_)
        
        return pedidosEntregados_

    def costoPedido(self, idPedido):
        totalPedido = 0
        for pedido_ in self.__pedidos:
            if pedido_.get_id() == idPedido:
                totalPedido = pedido_.precioPedido()
        
        return totalPedido

   
    def comprobarEmail(email):

        match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if match:
           return True
        else:
            return False

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        result = self.comprobarEmail(email) 
        if result == True:
            self.__email = email
        else:
            print("El correo ingresado no es valido")

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_pedidos(self):
        return self.__pedidos
    
    def set_pedidos(self, pedidos):
        self.__pedidos = pedidos



