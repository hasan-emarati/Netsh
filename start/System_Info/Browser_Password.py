# import os
# from selenium import webdriver


# chrome_driver_path = os.path.join(os.getcwd(), "chromedriver.exe")
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') 
# with webdriver.Chrome(options=chrome_options) as driver:
#     driver.get("chrome://settings/passwords")
#     password_elements = driver.find_elements('//span[@class="password"]')
#     for element in password_elements:
#         print(element.text)

import win32crypt
import sqlite3

# مسیر فایل پروفایل مرورگر Firefox
firefox_profile_path = 'C:/Users/seyed hasan emarati/AppData/Roaming/Mozilla/Firefox/Profiles/z7edlvnv.default-release'

# اتصال به دیتابیس logins.sqlite در پروفایل مرورگر Firefox
conn = sqlite3.connect(f"{firefox_profile_path}/logins.sqlite")
cursor = conn.cursor()

# اجرای کوئری برای بازیابی اطلاعات از جدول logins در دیتابیس

# پردازش رکوردهای بازگردانده شده از دیتابیس
for row in cursor.fetchall():
    hostname = row[0]
    encrypted_username = row[1]
    encrypted_password = row[2]
    
    # رمزگشایی نام کاربری و رمز عبور
    username = win32crypt.CryptUnprotectData(encrypted_username, None, None, None, 0)[1].decode('utf-8')
    password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode('utf-8')

    print(f"Hostname: {hostname}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("------------------------------------")

# بستن اتصال به دیتابیس
cursor.close()
conn.close()
