from Server import Server
import sys
import _thread

def main():
    """
        app startup function
        this function controls the server and client threads
    """

    host = "0.0.0.0" #defines localhost ip for the server

    #condition to recieve the port from system args (8080 if none is passed)
    if len(sys.argv) == 1:
        port = 8080
    else:
        port = int(sys.argv[1])

    server = Server(host, port) #create server instance

    server.createSocket() #create server's socket
    server.bindSocket() #actually create socket's connection

    #main loop to accept many connections
    while True:
        try:
            conn, addr = server.acceptConnection() #get connection class and address from new client
  
            _thread.start_new_thread(server.run, (conn, addr)) #start new thread for client

        except KeyboardInterrupt:
            break

    print('closing socket and shutting down server...')
    server.closeServer()
    print('goodbye!') #close socket after loop


if __name__ == "__main__":
    main()