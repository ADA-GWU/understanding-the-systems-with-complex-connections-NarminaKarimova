import socket
import sys
import time

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

        s.close()  # Close the socket when done

    except ConnectionRefusedError:
        print(f"Error: Server on port {port} is not running. Please start the server.")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <port1> <port2> ...")
        sys.exit(1)

    ports = [int(port) for port in sys.argv[1:]]  # Parse command-line arguments as integers

    # Create a list to store all sockets
    sockets = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define 's' here
        connect_to_server(port)
        sockets.append(s)  # Add the socket to the list

    # Wait for 2 seconds before exiting
    time.sleep(2)

    # Close all sockets
    for s in sockets:
        s.close()
