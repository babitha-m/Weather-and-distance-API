import socket
import requests

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the server's public IP address or domain name
host = '10.30.204.249'

# define port number
port = 9999

# connect to the server
client_socket.connect((host, port))


# send a message to the server
print("\n\n------------------------ WEATHER N DISTANCE TRACKER --------------------------\n\n")
while 1:
    a = input('----> Select one from the following options \n1. Get weather for you city      \n2. Get distance between two cities\n')
    if a=='1':
        opt = '1'
        client_socket.send(opt.encode())
        message = input('Enter the name of your city: ')
        client_socket.send(message.encode('utf-8'))
        dummy = 'city'
        client_socket.send(dummy.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        a = data.split(' ')
        temp = a[0]
        humidity = a[1]
        description = ' '.join(a[2:])
        print("\nThe weather report for your city is:\n")
        print(f"Temperature: {temp}\n\nHumidity: {humidity}\n\nDescription: {description}\n\n")
        print("----------------------------------------------------------------")
    
    if a=='2':
        opt = '2'
        client_socket.send(opt.encode())
        city1 = input('Enter the name of the first city: \n')
        client_socket.send(city1.encode('utf-8'))
        city2 = input('Enter the name of the second city: \n')
        client_socket.send(city2.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        data = data[:6]
        print(f"The distance between {city1} and {city2} is: {data} km\n\n")
        print("-----------------------------------------------------------------")


# close the connection
client_socket.close()
