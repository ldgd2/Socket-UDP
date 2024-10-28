import threading
from conexion import Conexion
from hilo_comunicacion import HiloComunicacion

class HiloConexiones(threading.Thread):
    def __init__(self, server_socket, servidor):
        super().__init__()
        self.server_socket = server_socket
        self.servidor = servidor
        self.activo = True
        # Diccionario para rastrear qué clientes ya se notificaron como activos
        self.clientes_notificados = set()

    def run(self):
        while self.activo:
            try:
                # Recibir mensaje y dirección del cliente
                data, direccion = self.server_socket.recvfrom(1024)
                mensaje = data.decode()

                # Verificar si la dirección ya tiene una conexión activa
                conexion_existente = self.servidor.get_conexion(direccion)

                if conexion_existente:
                    # Cliente ya está conectado
                    if direccion not in self.clientes_notificados:
                        print(f"Cliente {direccion[0]} ya tiene una conexión activa con ID de sesión {conexion_existente.id_sesion}.")
                        self.clientes_notificados.add(direccion)

                    # Mostrar el mensaje en el formato especificado una sola vez
                    print(f"Mensaje de ({direccion[0]}, {conexion_existente.id_sesion}): {mensaje}")
                    # Procesar el mensaje en el hilo de comunicación existente
                    conexion_existente.hilo_comunicacion.procesar_mensaje(mensaje)
                else:
                    # Cliente nuevo: crear una nueva conexión y un hilo de comunicación
                    nueva_conexion = Conexion(direccion, self.server_socket)
                    hilo_comunicacion = HiloComunicacion(self.server_socket, direccion)
                    nueva_conexion.hilo_comunicacion = hilo_comunicacion
                    self.servidor.agregar_conexion(nueva_conexion)

                    # Agregar al conjunto de clientes notificados
                    self.clientes_notificados.add(direccion)
                    
                    # Mostrar el mensaje de primera conexión y el mensaje recibido
                    print(f"Conexión aceptada desde {direccion} con ID de sesión {nueva_conexion.id_sesion}.")
                    print(f"Mensaje de ({direccion[0]}, {nueva_conexion.id_sesion}): {mensaje}")
                    
                    # Iniciar el hilo de comunicación y procesar el mensaje inicial
                    hilo_comunicacion.start()
                    hilo_comunicacion.procesar_mensaje(mensaje)

            except Exception as e:
                print(f"Error en la aceptación de conexiones: {e}")
                self.activo = False

    def detener(self):
        self.activo = False
