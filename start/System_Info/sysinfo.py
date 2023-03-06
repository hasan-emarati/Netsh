import platform
import psutil
import win32api
import subprocess

def Get_System_Info():
    # Get system information
    system_info = {
        "System ID": platform.uname().node,
        "Operating System": platform.system(),
        "OS Version": platform.release(),
        "Processor": platform.processor(),
        "Ram": psutil.virtual_memory().total,
        "Disk Info": psutil.disk_usage('/'),
        "Username Run app": win32api.GetUserName(),
    }
    
    # Print system information
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    # Get user information
    users = psutil.users()
    for user in users:
        print(f"User Info: {user}")
    
    # Get list of active users
    all_users = subprocess.check_output("net user", shell=True).decode('utf-8')
    all_users = all_users[all_users.find("User accounts for") + len("User accounts for"):all_users.find("The command completed successfully.")]
    all_users = [user.strip() for user in all_users.split() if "@" not in user and "\\" not in user and "----" not in user and user != ""]
    print(f"List of Users: {all_users}")

Get_System_Info()
