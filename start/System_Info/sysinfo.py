import platform
import psutil
import win32api
import subprocess

def System_Info():
    # Get system information
    system_info = {
        "SysID": platform.uname().node,
        "OperSys": platform.system(),
        "OSVersion": platform.release(),
        "Processor": platform.processor(),
        "Ram": psutil.virtual_memory().total,
        "Disk": psutil.disk_usage('/'),
        "UserName": win32api.GetUserName(),
    }
    # print (system_info["UserName"])
    # Print system information
    for key, value in system_info.items():
        SysInfo = f"{key}: {value}"
    return system_info


System_Info()

def All_Users():

    # Get list of active users
    all_users = subprocess.check_output("net user", shell=True).decode('utf-8')
    all_users = all_users[all_users.find("User accounts for") + len("User accounts for"):all_users.find("The command completed successfully.")]
    all_users = [user.strip() for user in all_users.split() if "@" not in user and "\\" not in user and "----" not in user and user != ""]
    print(f"List of Users: {all_users}")
    return all_users

# All_Users()