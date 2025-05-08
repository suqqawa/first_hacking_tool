import socket
import termcolor 
def scan(targets,ports):
    for port in range(len(ports)):
        scan_port(targets,port)

def scan_port(ipadress,port):
    try:            #при удачном сканировании
        sock=socket.socket()#инициализируем сокет
        #устанавливаем соединение:
        sock.connect((ipadress,port))
        print(f"[))] PORT {port} IS OPENED")
    except:
        print(f"[NO] PORT {port} is closed")
#получаем инфу от пользователя
targets=input("[XD] Enter Targets To Scan(you can split them by \",\"): ")
ports=[]
how_many_ports=int(input("[XD] Enter How Many Ports You Want To Scan: "))
for i in range (how_many_ports):
    i=int(input("[XD] Enter Port Number: "))
    ports.append(i)
if "," in targets:
    print("[>>] Scaning Multiple Targets")
    for ip_adr in targets.split(","):
        scan(ip_adr,ports)