import socket
import time

def receive_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 30001))
    data = s.recv(30000)
    print(repr(data))


while True:
    time.sleep(2) # Delaying new requests to avoid crashing the game
    receive_data()
    print('''
    Updating in 2 seconds (to avoid crashing the game)
    ''')
