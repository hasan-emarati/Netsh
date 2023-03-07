import subprocess
import wifiPassword
import os
import re

def WifiPassword():

    Get_Profiles = subprocess.getoutput("netsh wlan show profiles")
    regex = r"All User Profile\s+:\s+(.*)"
    matches = re.findall(regex, Get_Profiles)
    profiles = [match for match in matches]
    for len in profiles : 
        Wifi_password = subprocess.getoutput("wifipassword " , len)
        print (Wifi_password)
        return Wifi_password

# WifiPassword()


