import socket
import requests
import math

def get_data(city):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=29210f4a374ac29580711aca73f572e9&units=metric")
        if response.status_code == 200:
            print(f"sucessfully fetched the data for city {city}")
            return response.json()
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")


def get_lat_long(city):
    # Construct query parameters
    api_key = '1b14acf395804aaead760465db62ced4'
    # Base URL for OpenCage Geocoding API
    base_url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {
        'q': city,
        'key': api_key
    }
    # Send request to OpenCage API
    response = requests.get(base_url, params=params)

    # Parse response as JSON
    data = response.json()
    # Extract latitude and longitude from response
    lat = data['results'][0]['geometry']['lat']
    lng = data['results'][0]['geometry']['lng']
    # Return latitude and longitude as tuple
    return (lat, lng)

def get_distance(city1,city2): 
    lat1, lng1 = get_lat_long(city1)
    lat2, lng2 = get_lat_long(city2)
    radius = 6371  # radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlng / 2) * math.sin(dlng / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the server's public IP address or domain name
host = '192.168.181.210'

# define port number
port = 9999

# bind the socket object to the host and port
server_socket.bind((host, port))

# wait for client connection
server_socket.listen(1)

# print message to indicate server is waiting for connection
print('Server waiting for connection...')

# accept client connection
conn, addr = server_socket.accept()

# print message to indicate that connection has been established
print('Connected by', addr)

while True:
    # receive message from client
    data1 = conn.recv(1024).decode('utf-8')
    data2 = conn.recv(1024).decode('utf-8')
    data3 = conn.recv(1024).decode('utf-8')
    if not data1 or not data2 or not data3:
        break
    
    if data1=='1':
        result = get_data(data2)
        conn.sendall(str(result).encode('utf-8'))
        
        
    elif data1=='2':
        result = get_distance(data2,data3)
        conn.sendall(str(result).encode('utf-8'))
        
    

# close the connection
conn.close()
