import re
import os

output = """Profiles on interface Wi-Fi:

Group policy profiles (read only)
---------------------------------
    <None>

User profiles
-------------
    All User Profile     : Mohito
    All User Profile     : CABIN-17
    All User Profile     : LinkTest
    All User Profile     : Uplink"""
regex = r"All User Profile\s+:\s+(.*)"
matches = re.findall(regex, output)
profiles = [match for match in matches]
print(profiles)


    
