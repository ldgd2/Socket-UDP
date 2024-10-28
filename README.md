Proyecto de Sockets UDP - Sistemas Distribuidos

Descripción
Este proyecto implementa un sistema de comunicación basado en Sockets UDP en Python, diseñado para permitir la conexión de múltiples clientes a un servidor. Fue desarrollado como parte de la materia Sistemas Distribuidos para demostrar el uso de sockets en la gestión de conexiones concurrentes en un entorno distribuido.

El servidor UDP escucha en un puerto específico, recibe mensajes de los clientes y responde a cada uno, utilizando hilos para gestionar cada conexión sin bloquear el funcionamiento del servidor.

Finalidad
Este proyecto sirve para ilustrar conceptos clave en redes y sistemas distribuidos:

Comunicación con Sockets UDP: Para enviar y recibir mensajes sin conexión (stateless).
Hilos (threads): Para manejar múltiples conexiones concurrentes.
Gestión de Sesiones: El servidor identifica y mantiene una sesión activa para cada cliente.
Requisitos para la Ejecución
Python: Versión 3.6 o superior.
Librerías Estándar de Python (no se requieren librerías externas):
socket: Para la comunicación entre cliente y servidor.
threading: Para el manejo de múltiples hilos.
uuid: Para generar identificadores únicos de sesión.
Asegúrate de tener Python instalado y de que tu entorno pueda ejecutar scripts de Python desde la línea de comandos.

Estructura del Proyecto y Explicación de las Clases
El proyecto está organizado en varias clases que cumplen roles específicos en la gestión de la comunicación:

main.py: Inicia el servidor y permite la recepción de conexiones. Este es el punto de entrada del servidor.

servidor.py: Contiene la clase Servidor, que configura el socket UDP y mantiene una lista de conexiones activas (cada una con un identificador único). Su función principal es gestionar y almacenar las conexiones activas mediante un diccionario, lo cual facilita el acceso y actualización de cada conexión existente.

hilo_conexiones.py: Define la clase HiloConexiones, que es responsable de aceptar las conexiones entrantes. Este hilo principal recibe los mensajes iniciales de cada cliente y verifica si ya existe una conexión activa con ese cliente. Si es una nueva conexión, se crea una entrada en la lista de conexiones; si ya existe, se reutiliza la conexión activa.

hilo_comunicacion.py: Define la clase HiloComunicacion, que maneja la comunicación directa con cada cliente. Una vez que se establece la conexión, HiloComunicacion recibe y procesa los mensajes de ese cliente específico. Este hilo se encarga de enviar una respuesta para cada mensaje recibido sin duplicar la creación de hilos innecesarios.

conexion.py: Contiene la clase Conexion, que almacena la información de cada conexión, incluyendo:

ID de Sesión (id_sesion): Un identificador único generado para cada cliente mediante uuid.
Dirección (direccion): IP y puerto del cliente.
Socket: Referencia al socket de comunicación.
Hilo de Comunicación (hilo_comunicacion): Hilo asignado a cada conexión para gestionar la comunicación.
Diagrama de Flujo Básico
Inicio del Servidor: Ejecutando main.py se inicia el servidor UDP en el puerto especificado.
Conexión del Cliente: Cada cliente se conecta y envía mensajes, que son recibidos por HiloConexiones.
Gestión de Mensajes: HiloComunicacion procesa cada mensaje del cliente y el servidor responde de acuerdo a la sesión del cliente.
Desconexión: La sesión permanece activa hasta que el servidor o el cliente se desconecten.
Uso
Iniciar el Servidor: Ejecuta main.py para iniciar el servidor en localhost y en el puerto especificado.


python main.py

Ejecutar el Cliente: Ejecuta cliente.py en otra terminal para conectarte al servidor y enviar mensajes.


python cliente.py

Enviar Mensajes: En el cliente, escribe un mensaje y presiona Enter. El servidor responderá a cada mensaje recibido, indicando el mensaje y la dirección del cliente en el formato:

Mensaje de (IP, ID): <contenido del mensaje>
Ejemplo de Ejecución

Servidor:

Servidor UDP escuchando en localhost:8080
Conexión aceptada desde ('127.0.0.1', 57000) con ID de sesión <ID único>
Mensaje de (127.0.0.1, <ID>): Hola, servidor!

Cliente:

Escribe un mensaje ('salir' para desconectar): Hola, servidor!
Respuesta del servidor: Tu mensaje fue: Hola, servidor!
