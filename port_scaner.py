import socket
import termcolor 
def scan(targets,ports):
    for port in range(len(ports)):
        print(f"[*] Scaning port {ports[port]}")
        scan_port(targets,port)

def scan_in_range(targets,ports):
    for port in range(1,ports[0]+1):
        print(f"[*] Scaning port {port}")
        scan_port_in_range(targets,port)

def scan_port_in_range(ipadress,port):
    try:            #при удачном сканировании
        sock=socket.socket()#инициализируем сокет
        #устанавливаем соединение:
        sock.connect((ipadress,port))
        print(f"[+] PORT {port} IS OPENED")
        sock.close()
    except:
        pass


def scan_port(ipadress,port):
    try:            #при удачном сканировании
        sock=socket.socket()#инициализируем сокет
        #устанавливаем соединение:
        sock.connect((ipadress,port))
        print(f"[+] PORT {ports[port]} IS OPENED")
        sock.close()
    except:
        print(f"[-] PORT {ports[port]} is closed")
#получаем инфу от пользователя
targets=input("[XD] Enter Targets To Scan(you can split them by \",\"): ")
ports=[]
choose=int(input("""CHOSE OPTIONS:
      1.Scan certan ports
      2.Scan range of ports(from "1" to input)  """))
if choose==1:
    how_many_ports=int(input("[XD] Enter How Many Ports You Want To Scan: "))
    for i in range (how_many_ports):
        i=int(input("[XD] Enter Port Number: "))
        ports.append(i)
    if "," in targets:
        print("[>>] Scaning Multiple Targets")
        for ip_adr in targets.split(","):
            print(f"[!!] Scaning {ip_adr}")
            scan(ip_adr,ports)
        
    else:
        print(f"[!!] Scaning {targets}")
        scan(targets,ports)
if choose ==2:
    i=int(input("[XD] Enter Port Number: "))
    ports.append(i)
    if "," in targets:
        print("[>>] Scaning Multiple Targets")
        for ip_adr in targets.split(","):
            print(f"[!!] Scaning {ip_adr}")
            scan_in_range(ip_adr,ports)
        
    else:
        print(f"[!!] Scaning {targets}")
        scan_in_range(targets,ports)
