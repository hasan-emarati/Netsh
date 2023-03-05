import platform
import psutil
import socket
import netifaces
import concurrent.futures

print("          System Info\n__________________________________\n")
print(" System ID : ", platform.uname().node)
System_ID = platform.uname().node
print(" Operating System : ", platform.system())
Operating_System = platform.system()
print(" OS Version : ", platform.release())
OS_Version = platform.release()
print(" Processor : ", platform.processor())
Processor = platform.processor()
Ram = psutil.virtual_memory().total
print(" Ram : ", Ram, "bytes")
Disk = psutil.disk_usage('/')
print(" Disk Info : ", Disk, " GB")
print("           Network\n____________________________________\n")
print("IP Address In Internet : ", socket.gethostbyname(socket.gethostname()))
Internet_Ip_Address = socket.gethostbyname(socket.gethostname())
Local_Ip_Address = socket.gethostbyname('localhost')
hostname = socket.gethostname()
print("Hostname : ", hostname)
print('Local Ip Address : ', Local_Ip_Address)
All_Nics = psutil.net_if_addrs()
for nic, addrs in All_Nics.items():
    for addr in addrs:
        if addr.family == netifaces.AF_INET:
            Enternet = f"{nic} : {addr.address}"
            print(Enternet)

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect(('localhost', port))
            return port
        except:
            return None

def find_open_ports():
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(check_port, port) for port in range(1, 65536)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

print("Open ports:", find_open_ports())


