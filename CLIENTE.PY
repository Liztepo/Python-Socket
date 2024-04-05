import socket

# Dirección IP y puerto del servidor
SERVER_IP = input('192.168.8.107')
PORT = 65432

# Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conectar el socket al servidor
    s.connect(('192.168.8.107' , PORT))

    while True:
        # Enviar mensaje al servidor
        message = input("Escriba su mensaje ('exit' para salir): ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode('utf-8'))
        
        # Recibir respuesta del servidor
        data = s.recv(1024)
        print(f"Respuesta del servidor: {data.decode('utf-8')}")
        