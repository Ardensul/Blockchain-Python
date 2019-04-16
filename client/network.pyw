import socket

def Ping7777():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 7777))
    sock.close()

    if result == 0:
        return True
    else:
        return False
