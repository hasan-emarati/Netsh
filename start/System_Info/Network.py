import psutil
import socket
import netifaces
import concurrent.futures
from selenium import webdriver


def get_network_info():
    print("\n           Network\n________________________________________________________________\n")
    
    # Get Internet IP address
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        internet_ip_address = s.getsockname()[0]
        print("IP Address In Local Network : ", internet_ip_address)
        
    # Get local IP address and hostname
    local_ip_address = socket.gethostbyname('localhost')
    hostname = socket.gethostname()
    print("Hostname : ", hostname)
    print('Local Ip Address : ', local_ip_address)
    
    # Get network interfaces and addresses
    all_nics = psutil.net_if_addrs()
    for nic, addrs in all_nics.items():
        for addr in addrs:
            if addr.family == netifaces.AF_INET:
                network_address = f"{nic} : {addr.address}"
                print(network_address)

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
        
    return internet_ip_address, local_ip_address, hostname, all_nics, open_ports

get_network_info()


