import socket

# Function to connect to a server and send/receive data
def connect_to_server(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', port))

        while True:
            # Input number
            number = input(f"Enter a number (connected to port {port}, 'exit' to quit): ")
            if number.lower() == 'exit':
                break

            # Send the number to the server
            s.send(number.encode())

            # Receive and print the server's response
            response = s.recv(1024).decode()
            print(f"Server response from port {port}: {response}")

    except ConnectionRefusedError:
        print(f"Error: Server on port {port} is not running. Please start the server.")
    except KeyboardInterrupt:
        pass
    finally:
        s.close()

if __name__ == "__main__":
    ports = [9001]

    for port in ports:
        connect_to_server(port)
