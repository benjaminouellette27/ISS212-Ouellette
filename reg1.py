'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use command: python reg1.py SOFTWARE
Remember to run in windows command prompt
'''

#import modules
import sys
import winreg

try:
    #connect to windows registry
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    # get registry key path
    key_path = sys.argv[1]
    # open the key path
    key = winreg.OpenKey(reg, key_path)

    # print infomation regaring the registry key.
    print(f"Analyzing {key_path} in Windows registry...")
    last_modified = winreg.QueryInfoKey(key)[2]
    print(f"Last modified: {last_modified} [UTC]")

    # looping through subkeys.
    try:
        for i in range(winreg.QueryInfoKey(key)[1]):
            subkey_name = winreg.EnumKey(key, i)
            print("Subkey:", subkey_name)

            subkey = winreg.OpenKey(key, subkey_name)

            # looping through all the values found within the subkeys.
            try:
                j = 0
                while True:
                    try:
                        value_name, value_data, _ = winreg.EnumValue(subkey, j)
                        print(f"Name: {value_name}, Value path: {value_data}")
                        j += 1
                    #error handling
                    except OSError as e:
                        if e.errno == 259:
                            break
                        else:

                            raise
            #error handling
            except OSError:
                pass
            print("\n")

    #error handling
    except OSError as e:
        if e.errno == 259:
            pass
        else:
            raise
#error handling
except FileNotFoundError as e:
    print("Registry key not found:", e)
except PermissionError as e:
    print("Permission error:", e)
except Exception as e:
    print("An error occurred:", e)
