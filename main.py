from Server import Server
import sys

def main():
    host = "0.0.0.0"

    if len(sys.argv) == 1:
        port = 8080
    else:
        port = int(sys.argv[1])

    server = Server(host, port)

    server.createSocket()
    server.bindSocket()

    while True:
        server.acceptConnection()

        server.init()

        server.closeConnection()

    server.closeSocket()



if __name__ == "__main__":
    main()