import winreg
from selenium import webdriver


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

# installed_programs = get_installed_programs()
# print("\n             All installed programs\n________________________________________________________________\n")
# print(installed_programs)
# print("\n________________________________________________________________")