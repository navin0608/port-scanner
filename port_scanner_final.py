#!/usr/bin/env python3

import nmap
import ipaddress
import re
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
port_min = 0
port_max = 65535

print("\n****************************************************************")
print("\n**** PROPERTY OF PRANAV & NAVIN KUMAR ****")
print("\n****************************************************************")

# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    # If we enter an invalid ip address the try except block will go to the except block and say you entered an invalid ip address.
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        # The following line will only execute if the ip is valid.
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")


while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning all the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    # We pass the port numbers in by removing extra spaces that people sometimes enter. So if you enter 80 - 90 instead of 80-90 the program will still work.
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        # We're extracting the low end of the port scanner range the user want to scan.
        port_min = int(port_range_valid.group(1))
        # We're extracting the upper end of the port scanner range the user want to scan.
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
# We're looping over all of the ports in the specified range.
for port in range(port_min, port_max + 1):
    try:
        # The result is quite interesting to look at. You may want to inspect the dictionary it returns. 
        # It contains what was sent to the command line in addition to the port status we're after. 
      
        result = nm.scan(ip_add_entered, str(port))

        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
        print(f"Cannot scan port {port}.")