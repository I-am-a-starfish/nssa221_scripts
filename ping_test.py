#!/usr/bin/python3


# Shefali Maurya 1/30/2026
import socket
import os
import subprocess
import re

# if application should keep going
status=1

# gateway pattern
pattern = r"default via ([0-9.]+)"

result = subprocess.run(["ip", "r"], capture_output=True, text=True, check=True)
output = result.stdout
match = re.search(pattern, output)
gateway = match.group(1)

# options to display
menu = """
1. Display the default gateway
2. Test Local Connectivity
3. Test Remote Connectivity
4. Test DNS Resolution
5. Exit/quit the script
"""
# local test
loopback = '127.0.0.1'
# remote_ping_test 
RITserver= '129.21.3.17'
# DNS test
google = 'www.google.com'

def connSucc(ipAd):
    command = ["ping", "-c", "4", ipAd],
    
    try:

        output = subprocess.run(["ping", "-c", "4", ipAd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Connection to "+ipAd+" successful!")

    except subprocess.CalledProcessError:
        # the command returned a non-zero exit status, indicating failure
        print("Connection to "+ipAd+" unsuccessful")

    except OSError as e:
        print(f"Error executing ping command: {e}")


    
def options():
    option = input(menu)

    # Display default gateway
    if(option == "1"):
        print("Gateaway: "+gateway)

    # Test Local Connectivity
    elif(option == "2"):
        connSucc(gateway)

    # Test Remote Connectivity
    elif(option == "3"):
        connSucc(RITserver)

    elif(option == "4"):
        connSucc(google)

    elif(option == "5"):
        global status
        status=0
        print("Exit")
    else:
        print("Invalid input")


def main():
    while(status==1):
        options()

os.system('clear')
main()
