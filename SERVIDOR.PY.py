import socket

# Configuración del servidor
HOST = '0.0.0.0'  # Escucha en todas las interfaces de red
PORT = 65432  # Puerto para la conexión

# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Enlace del socket a la dirección y puerto especificados
    s.bind((HOST, PORT))
    # Escuchar conexiones entrantes
    s.listen()

    print("Esperando una conexión...")
    conn, addr = s.accept()
    with conn:
        print(f"Conexión establecida desde {addr}")

        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            print(f"Mensaje recibido del cliente: {data.decode('utf-8')}")
            # Enviar respuesta al cliente
            reply = input("Escriba su respuesta: ")
            conn.sendall(reply.encode('utf-8'))
            