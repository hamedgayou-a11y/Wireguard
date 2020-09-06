# TODO: A simple interface for installing ansible and running this project

import subprocess
import re
import os
import json
#########################################[Helper Functions Comments]####################################

def checkIPAddress(ip):
    '''
        enter the ip as string
        return True if valid else False
    '''
    try:
        pat = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$")
        if pat.match(ip):
            lst = ip.split('.')
            for p in lst:
                if p.__contains__("/"):
                    p = p.split("/")
                    if 0 >= int(p[1]) >= 32:
                        return False
                    p = p[0]
                p = int(p)
                if p > 255 or p < 0:
                    print("[-] ip is not valid")
                    return False
            return True
        else:
            print("[-] ip is not valid")
            return False
    except Exception as e:
        print(e)
        return False


#########################################[Basic Comments]###############################################

'''
ansible-playbook -i inventory/static-inventory.ini install.yaml
ansible-playbook -i inventory/static-inventory.ini config.yaml
ansible-playbook -i inventory/static-inventory.ini monitor.yaml
ansible-playbook -i inventory/static-inventory.ini addpeer.yaml
'''

#########################################[Global Vars Of Code]##########################################

helper_string = """
hello everybody, this is done by zerobits01(mmd-mrd)
you can find me through this ways:
gitlab: gitlab.com/zerobits01
gmail: zerobits0101@gmail.com

what do you wanna do?
1) installation
2) configuration and starting the service
3) monitoring
4) adding peer
5) exit

"""

install_command = ["ansible-playbook", "-i", "inventory/static-inventory.ini", "install.yaml"]
config_command  = ["ansible-playbook", "-i", "inventory/static-inventory.ini", "config.yaml"]
monitor_command = ["ansible-playbook", "-i", "inventory/static-inventory.ini", "monitor.yaml"]
add_peer_command= ["ansible-playbook", "-i", "inventory/static-inventory.ini", "addpeer.yaml"]
#########################################[CORE Part Of Code]############################################

def miningMonitorData(data):
    try:
        print("\n\n")
        print("*" * 20)
        pattern = re.compile(r"ok:\s*\[(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]\s*=>\s*(?P<data>\s*\{\s*.*\s*\}\s*)")
        all_data = pattern.findall(data)
        for gps in all_data:
            logs = json.loads(gps[1])
            logs = logs['msg'].replace("\'", "\"")
            print('-'*20)
            print(gps[0], ": ")
            print(logs)
            print("\n")
        print("*" * 20)
    except Exception as e:
        print(e)

def runInstall():
    install_command = "ansible-playbook -i inventory/static-inventory.ini install.yaml"
    output = os.system(install_command)
    if output == 0:
        print("[+] installed correctly.")
    else:
        print("[-] something went wrong!")



def runConfig():
    config_command = "ansible-playbook -i inventory/static-inventory.ini config.yaml"
    output = os.system(config_command)
    if output == 0:
        print("[+] configure and started.")
    else:
        print("[-] something went wrong!")



def runAddPeer():
    print("1) adding new peer ip and pubkey\n2) running command with existing yaml file\n")
    todo = int(input("> "))
    if todo == 1:
        print("enter the peer ip:")
        ip = input("ip> ")
        if checkIPAddress(ip):
            print("paste the peer public key here")
            pubkey = input("public key> ")

            with open("./roles/add_peer/defaults/main.yaml", 'a+') as f:
                try:
                    peer = f"  - ip: {ip}\n    pubkey: {pubkey}\n"
                    f.write(peer)
                except Exception as e:
                    print(e)
        else:
            print("[!] the ip entered is not valid")

    add_peer_command = "ansible-playbook -i inventory/static-inventory.ini addpeer.yaml"
    output = os.system(add_peer_command)
    if output == 0:
        print("[+] peer added.")
    else:
        print("[-] something went wrong!")



def runMonitor():
    output = subprocess.check_output(monitor_command)
    miningMonitorData(output.decode('utf-8'))
    return output


#########################################[CLI Part Of Code]#############################################


def CLI():
    while True:
        try:
            print(helper_string)

            todo = int(input("> "))

            if todo == 1:
                runInstall()
            elif todo == 2:
                runConfig()
            elif todo == 3:
                runMonitor()
            elif todo == 4:
                runAddPeer()
            elif todo == 5:
                print("bye bye! :)")
                exit(0)
            else:
                print("enter a valid option :(")
        except TypeError:
            print("please enter a number, what you have entered is not valid")
        except Exception as e:
            print(e)


#########################################[MAIN Part Of Code]############################################


def main():
    CLI()


if __name__ == "__main__":
    main()