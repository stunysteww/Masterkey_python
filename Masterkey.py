import subprocess
import re
#Masterkey
Masterkey= "shashankcodes"
#Asking for Masterkey
EnterMasterKey = input("Enter your Masterkey")
#Veryfing whther the user has entered the correct Masterkey or not
if EnterMasterKey == Masterkey:
    print("Yup that was the correct masterkey")
    print("And these are your wifi passwords")

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = []
if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile) 

            for x in range(len(wifi_list)):
                print(wifi_list[x]) 
                print("Thanks for using this program. If you liked it please support me on https://www.buymeacoffee.com/shashankstew")

