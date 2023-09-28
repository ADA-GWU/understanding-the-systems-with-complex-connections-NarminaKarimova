import socket
import sys

# Function to handle a single client connection
def handle_client(c):
    while True:
        try:
            number = c.recv(1024).decode()
            if not number:
                break

            # Double the input number
            result = str(int(number) * 2)
            print('Doubled number from client input:', result)
            c.send(result.encode())
        except ValueError:
            c.send("Invalid input. Please enter a number.".encode())
    c.close()

def main():
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        return

    port = int(sys.argv[1])
    s = socket.socket()
    s.bind(('', port))
    print(f'Server bound to port: {port}')
    s.listen(1)

    print(f'Server is listening on port {port}')

    while True:
        c, addr = s.accept()
        print('Connected to client:', addr)
        handle_client(c)

if __name__ == "__main__":
    main()
