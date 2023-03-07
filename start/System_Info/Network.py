import psutil
import socket
import netifaces
import concurrent.futures
from selenium import webdriver


def get_network_info():
      
    # Get network interfaces and addresses
    all_nics = psutil.net_if_addrs()
    for nic, addrs in all_nics.items():
        for addr in addrs:
            if addr.family == netifaces.AF_INET:
                network_address = f"{nic} : {addr.address}"
                print(network_address)

get_network_info()

# get_network_info()

def Local_Ip():

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        internet_ip_address = s.getsockname()[0]
        print("IP Address In Local Network : ", internet_ip_address)
        return internet_ip_address
    
# Local_Ip()

def HostName():
    
    # Get local IP address and hostname
    local_ip_address = socket.gethostbyname('localhost')
    hostname = socket.gethostname()
    print("Hostname : ", hostname)
    print('Local Ip Address : ', local_ip_address)
    return hostname , local_ip_address

def OpenPorts():
    # Find open ports
    def check_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect(('localhost', port))
                return port
            except:
                return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(check_port, port) for port in range(1, 65536)]
        open_ports = [future.result() for future in concurrent.futures.as_completed(futures) if future.result()]
        print("Open ports:", open_ports)
        return open_ports
    
# OpenPorts()