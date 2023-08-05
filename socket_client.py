#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-08-04 20:27:26

import begin
import socket

def client():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


@begin.start
def main(arg1 = None):
    client()
