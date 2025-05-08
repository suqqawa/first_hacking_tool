import socket
import termcolor 
def scan(targets,ports):
    for port in range(len(ports)):
        print(termcolor.colored(f"[*] Scaning port {port}",'blue'))
        scan_port(targets,port)

def scan_in_range(targets,ports):
    for port in range(1,ports[0]+1):
        print(termcolor.colored(f"[*] Scaning port {port}",'blue'))
        scan_port_in_range(targets,port)

def scan_port_in_range(ipadress,port):
    try:            #при удачном сканировании
        sock=socket.socket()#инициализируем сокет
        #устанавливаем соединение:
        sock.connect((ipadress,port))
        print(termcolor.colored(f"[+] PORT {port} IS OPENED",'green'))
        sock.close()
    except:
        pass


def scan_port(ipadress,port):
    try:            #при удачном сканировании
        sock=socket.socket()#инициализируем сокет
        #устанавливаем соединение:
        sock.connect((ipadress,port))
        print(termcolor.colored(f"[+] PORT {ports[port]} IS OPENED",'green'))
        sock.close()
    except:
        print(termcolor.colored(f"[-] PORT {ports[port]} is closed",color='red'))
#получаем инфу от пользователя
targets=input("[XD] Enter Targets To Scan(you can split them by \",\"): ")
ports=[]
choose=int(input("""CHOSE OPTIONS:
      1.Scan certan ports
      2.Scan range of ports(from "1" to input)  """))
if choose==1:
    how_many_ports=int(input("[XD] Enter How Many Ports You Want To Scan: "))
    for i in range (how_many_ports):
        i=int(input(termcolor.colored("[XD] Enter Port Number: ",'pink')))
        ports.append(i)
    if "," in targets:
        print(termcolor.colored("\n"+"[>>] Scaning Multiple Targets",'orange'))
        for ip_adr in targets.split(","):
            print(termcolor.colored("\n"+f"[!!] Scaning {ip_adr}",'purple'))
            scan(ip_adr,ports)
        
    else:
        print(termcolor.colored("\n"+f"[!!] Scaning {targets}",'purple'))
        scan(targets,ports)
if choose ==2:
    i=int(input(termcolor.colored("[XD] Enter Port Number: ",'yellow')))
    ports.append(i)
    if "," in targets:
        print(termcolor.colored("\n"+"[>>] Scaning Multiple Targets",'cyan'))
        for ip_adr in targets.split(","):
            print(termcolor.colored("\n"+f"[!!] Scaning {ip_adr}",'magenta'))
            scan_in_range(ip_adr,ports)
        
    else:
        print(termcolor.colored("\n"+f"[!!] Scaning {targets}",'purple'))
        scan_in_range(targets,ports)
    

