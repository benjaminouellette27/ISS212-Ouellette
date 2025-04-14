'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use command: python reg2.py SOFTWARE
'''

#import modules
import sys
from regipy.registry import RegistryHive


try:
    #get hive path and load the registry hive.
    hive_path = sys.argv[1]
    reg = RegistryHive(hive_path)

    # print the hive path being analyzed
    print(f"Analyzing {hive_path}...")
    # access the registry key.
    software_key = reg.get_key(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    # if the specified key is found:
    # extract and display specific values.
    if software_key:
        print("\tProduct name:", software_key.get_value("ProductName"))
        print("\tCurrentVersion:", software_key.get_value("CurrentVersion"))
        print("\tServicePack:", software_key.get_value("CSDVersion"))
        print("\tProductID:", software_key.get_value("ProductId"))

    # error handling
    else:
        print("Subkey 'CurrentVersion' not found in the provided registry file.")

# error handling
except FileNotFoundError as exception:
    print(f"Registry hive file not found: {exception}")
except Exception as exception:
    print(f"An error occurred: {exception}")
