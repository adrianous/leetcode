import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("move:1_1".encode('utf-8'), ('192.168.11.200', 12324))
time.sleep(2.5)
s.sendto("move:0_0".encode('utf-8'), ('192.168.11.200', 12324))
s.close()

