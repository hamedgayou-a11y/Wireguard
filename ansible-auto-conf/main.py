# TODO: A simple interface for installing ansible and running this project

import subprocess

'''
ansible-playbook -i inventory/static-inventory.ini install.yaml
ansible-playbook -i inventory/static-inventory.ini config.yaml
ansible-playbook -i inventory/static-inventory.ini monitor.yaml
ansible-playbook -i inventory/static-inventory.ini addpeer.yaml
'''

def runInstall():
    # TODO: only running the ansible command
    pass

def runConfig():
    # TODO: only running the command
    pass

def runAddPeer():
    # TODO: getting the peer info,
    #           adding to roles/add_peer/defaults/main.yaml
    #            running the command
    pass

def runMonitor():
    # TODO: running the command and return the answer as a dictionary
    pass

def CLI():
    # TODO: Command Line user Interface
    pass

#########################################[MAIN Part Of Code]#########################################

def main():
    CLI()
    pass

if __name__ == "__main__":
    main()