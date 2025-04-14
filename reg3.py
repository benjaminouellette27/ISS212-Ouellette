'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use Command: python reg3.py SYSTEM
'''

#import modules
import winreg
import sys

# find the currently active control set.
def getCurrentControlSet():
    try:
        hkey_local_machine = winreg.HKEY_LOCAL_MACHINE
        select_subkey = "SYSTEM\\Select"

        with winreg.OpenKey(hkey_local_machine, select_subkey) as key:
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                value_name, value_data, _ = winreg.EnumValue(key, i)
                if value_name == "Current":
                    return value_data
    # error handling
    except FileNotFoundError as exception:
        print("Couldn't find SYSTEM\\Select key ", exception)

# prints service info in clean, humanreadable format.
def getServiceInfo(dictionary):
    serviceType = {
        1: "Kernel device driver", 2: "File system driver", 4: "Arguments for an adapter",
        8: "File system driver interpreter", 16: "Own process", 32: "Share process",
        272: "Independent interactive program", 288: "Shared interactive program"
    }
    print(" Service name: %s" % dictionary["SERVICE_NAME"])
    if "DisplayName" in dictionary:
        print(" Display name: %s" % dictionary["DisplayName"])

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType.get(dictionary["Type"], "Unknown"))

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")

# extracting parameters of a service from its registry subkey.
def serviceParams(subkey):
    service = {}
    service["SERVICE_NAME"] = subkey
    service["ModifiedTime"] = winreg.QueryInfoKey(subkey)[2]

    try:
        for i in range(0, winreg.QueryInfoKey(subkey)[1]):
            value_name, value_data, _ = winreg.EnumValue(subkey, i)
            service[value_name] = value_data
    # error handling
    except OSError as exception:
        print("Error accessing registry subkey ", exception)

    getServiceInfo(service)

# listing all service under the current control set.
def servicesKey(controlset):
    serviceskey = "SYSTEM\\ControlSet00%d\\Services" % controlset
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, serviceskey) as key:
            for i in range(0, winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                serviceParams(subkey)
    # error handling
    except FileNotFoundError as exception:
        print("Couldn't find Services key ", exception)

# executing the main function.
if __name__ == "__main__":
    controlset = getCurrentControlSet()
    if controlset is not None:
        servicesKey(controlset)
