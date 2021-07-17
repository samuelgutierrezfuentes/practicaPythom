from Cliente import Cliente
from Direccion import Direccion
from Repartidor import Repartidor
from Producto import Producto
from Pedido import Pedido

direccion = Direccion('calle la virgen', 4, 2,'D', 47008, 'Valencia')
cliente_1 = Cliente('nombreCliente', 31002133, direccion )
repartidor_1 = Repartidor('nombre repartidor', 31009233, 1200)
# Creo los productos
producto_1 = Producto(1, 'Producto_1', 10, 4)
producto_2 = Producto(2, 'Producto_2', 11, 5)
producto_3 = Producto(3, 'Producto_3', 12, 6)
producto_4 = Producto(4, 'Producto_4', 13, 7)

# Definimos los pedidos entregados
pedido_1 = Pedido(1) # Pasamos parametros por constructor
pedido_1.set_entregado(True);
pedido_1.set_productos([producto_1, producto_2]) # Enviamos los productos

pedido_2 = Pedido(2)  # Pasamos parametros por constructor
pedido_2.set_entregado(True);
pedido_2.set_productos([producto_3, producto_4]) # Enviamos los productos

# Agregar pedidos entregados
cliente_1.set_pedidos([pedido_1, pedido_2])
repartidor_1.set_pedidos([pedido_1, pedido_2])
# Definimos los pedidos pendientes de entregadar
pedido_3 = Pedido(3) # Pasamos parametros por constructor
pedido_3.set_productos([producto_3, producto_2]) # Enviamos los productos

pedido_4 = Pedido(4)  # Pasamos parametros por constructor
pedido_4.set_productos([producto_3, producto_1]) # Enviamos los productos

# Agregar pedidos pendientes de entregar
cliente_1.agregarPedido(pedido_3)
cliente_1.agregarPedido(pedido_4)
repartidor_1.agregarPedido(pedido_3)
repartidor_1.agregarPedido(pedido_4)


# Agregar pedidos pendientes de entregar
cliente_1.agregarPedido(pedido_3)

#Validar la cantidad de pedidos que debe ser 4, 2 pedidos entregados y dos pendientes
print('Cantidad de pedidos: ', len(cliente_1.get_pedidos()))

#validar Cantidad de pedidos entregados
print('Cantidad de pedidos entregados: ', len(cliente_1.pedidosEntregados()))

# Función para obtener el producto mas caro que un cliente ha solicitado
def masCaro(cliente):
    productoMasCaro = None
    precioMasCaro = 0
    for pedidos in cliente.get_pedidos():
        for producto in pedidos.get_productos():
            if producto.get_precio() > precioMasCaro:
                precioMasCaro = producto.get_precio()
                productoMasCaro = producto
    print("Producto mas caro: ", productoMasCaro.get_nombre(), ", Precio: ", productoMasCaro.get_precio())

masCaro(cliente_1)

# Función para validar esi el repartidor tiene pedidos pendientes de entregar
def pedidosPendientes(repartidor):
    for pedido in repartidor.get_pedidos():
        if pedido.get_entregado() == False: # Si algun pedido es False en la prodiedad "Entregado", retornamos True
            return True    
    return False        
print('Tiene pedidos pendientes: ', pedidosPendientes(repartidor_1)) 
            



         


#print(pedido_1.get_id_pedido(), pedido_1.get_entregado(), pedido_1.get_productos())
#print(direccion.get_calle())
#print(cliente_1.get_nombre())
#print(repartidor_1.get_nombre())

