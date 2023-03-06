import subprocess

def Directory():
    
    Directory = subprocess.getoutput("dir /s")
    return Directory

print ("            All Directoryn\n________________________________________________________________\n")
print(Directory())
print("\n________________________________________________________________\n")