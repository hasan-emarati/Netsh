import pyudev
import shutil
import os

source_file = "file.txt"


startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
destination_file = os.path.join(startup_folder, 'file.txt')

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')


for device in iter(monitor.poll, None):
    if device.action == 'add':
        print('USB connected.')
        shutil.copy(source_file, destination_file)
        print(f'File copied to {destination_file}.')
        break






# import subprocess
# import os

# startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
# src_path = r'C:\test\sample.txt'
# dst_path = os.path.join(startup_path, 'sample.txt')
# subprocess.run(['cmd', '/c', 'copy', src_path, dst_path])
