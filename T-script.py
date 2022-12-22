#!/usr/bin/python3
import time
import os
import re

distro=""
#tools=["cewl","git","stegcracker","wpscan","smbclient","smbmap","curl","wget","nmap","vim","whatweb","gobuster","binwalk","wfuzz","hydra","john","hashcat","aircrack-ng","evil-winrm","steghide","recon-ng","whois","twint","reaver","metasploit","exploitdb","nikto","netdiscover","seclists","webshells","openvpn"]   
#tools=["cewl","git","stegcracker","wpscan","smbclient","smbmap","curl","wget","whatweb","vim","burpsuite"]
tools=["cewl","git","stegcracker","wpscan","smbclient"]
tools_exist=[]
tools_to_install=[]
ui_list=[]
garb=[]

#Arch or Debian?
def os_check(distro=distro):
    check=os.popen("cat /etc/os-release").read()
    x=check.split()
    #print(x)
    lists=[]
    for i in x:
        words=i.split()
        lists.append(words[0])
    #print(lists)
    for distro_type in lists: 
        if distro_type == "ID=arch" or distro_type == "ID_LIKE=arch":
            distro="arch"
            break
        elif distro_type == "ID=debian" or distro_type == "ID_LIKE=debian":
            distro="debian"
            break
        else:
            distro="can't find distro type!"
    print(f"distro type: {distro}")
    print("\n")

#Arch
def arch():
        blackarch=os.popen("sudo ls /etc/pacman.d/ | grep -i 'blackarch-mirrorlist'").read().strip()
        if blackarch != "blackarch-mirrorlist":    
            #sec1
            print("Installing black arch!")
            os.system("curl -O https://blackarch.org/strap.sh")
            os.system("echo 5ea40d49ecd14c2e024deecf90605426db97ea0c strap.sh | sha1sum -c")
            os.system("chmod +x strap.sh")
            os.system("./strap.sh")
            os.system("pacman -Syy")
        else:
           pass
       #sec2
       #banner1
        print("-----------------------------------")
        print("|            pakages              |")
        print("-----------------------------------")
        print("\n")
        for toolin in tools:
                tol=os.popen(f"pacman -Qe {toolin} 2>/dev/null | cut -d ' ' -f 1").read().strip()
                if toolin.lower() == tol.lower():
                        tools_exist.append(toolin)
                        print(f"{toolin} -----> already installed")
                else:
                        tools_to_install.append(toolin)
                        print(f"{toolin} -----> not installed")
        #sec3
        print("\n")
        #banner2
        print("-----------------------------------")
        print("| pakages which are not installed |")
        print("-----------------------------------")
        count=0
        for tni in tools_to_install:
                print(f"[{count}]  {tni}")
                count=count+1
        print("\n")
        print("ctrl+c to cancel")
        try:
            #5 sec
            time.sleep(100)
            #sec4
            for tool in tools:
                    print("install")
                    os.system(f"yes | sudo pacman -S {tool}")
        except KeyboardInterrupt:
            global userinput
            userinput="give"
        print("\n")
        list_for_userin=["x","c","e"]
        while userinput not in list_for_userin:
                userinput=str(input("exclude[x], choose[c] or exit[e] : "))
        #exclude
        if userinput.lower() == list_for_userin[0]:
                os.system("clear")
                #banner3
                print("-----------------------------------")
                print("|  select the pakages to exclude  |")
                print("-----------------------------------")
                print("\n")
                for index,value in enumerate(tools_to_install):
                        print(f"[{index}]  {value}")
                print("\n")
                userinput1=str(input("enter in this order - [0,2,3,4] : "))
                replaceing=userinput1.replace(","," ")
                ui_list=list(map(int,replaceing.split()))
                for i in ui_list:
                    if i in range(0,len(tools_to_install)+1):
                        tools_to_install.insert(i,"#")
                        tools_to_install.pop(i+1)
                    else:
                        print("not working")
                for i in tools_to_install:
                    if i == "#":
                        pass
                    else:
                        print("\n")
                        print(f"Installing  {i}")
                        os.system(f"yes | sudo pacman -S {i}")
                        print("\n")
                        os.system("clear")
                print("done!")
                       
        #choose
        elif userinput.lower() == list_for_userin[1]:
            os.system("clear")
            #banner4
            print("-----------------------------------")
            print("|       choose the pakages        |")
            print("-----------------------------------")
            print("\n")
            for index,value in enumerate(tools_to_install):
                print(f"[{index}]  {value}")
            print("\n")
            userinput2=str(input("enter in this order - [0,2,3,4] : "))
            replaceing=userinput2.replace(","," ")
            ui_list=list(map(int,replaceing.split()))
            print(ui_list)
            for i in ui_list:
                print("\n")
                print(f"Installing {tools_to_install[i]}")
                os.system(f"sudo pacman -S {tools_to_install[i]}")
                print("\n")
                os.system("clear")
            print("done!")

        #exit
        elif userinput.lower() == list_for_userin[2]:
            exit()
os_check()
arch()
#blacharch_check()
#debian
