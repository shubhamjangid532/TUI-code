from packages import *
import os
import getpass
os.system("clear")
MyDetails()
a = 1
while a == 1 :
        os.system("tput setaf 1")
        print("\t\t\t Hello MR. Thanks For Using My TUI")
        os.system("tput setaf 7")
        print("\t\t--------------------------------------------------")
        os.system("tput setaf 2")
        ip_add = input("Please Enter The IP Where You Want to Perform Operation : ")
        os.system("tput setaf 7")
        b = 1
        while b == 1:
            mainMenu(ip_add)
            os.system("tput setaf 7")

            print("Please Only Enter Number")
            ch1 = int(input("Enter Your Choice : "))
            if ch1 == 0 :
                print("""

                    You exit For Current Menu

                """)
                b = 2

            elif ch1 == 1 :
                basicOperation(ip_add)
                os.system("tput setaf 7")


            elif ch1 == 2 :
                packManagement(ip_add)
                os.system("tput setaf 7")


            elif ch1 == 3 :
                e = 1
                while e == 1 :
                    userManagement(ip_add)
                    os.system("tput setaf 7")


            elif ch1 == 4 :
                f = 1
                while f == 1 :
                    Networking(ip_add)
                    os.system("tput setaf 7")


            elif ch1 == 5 :
                f = 1
                while f == 1 :
                    serviceManagement(ip_add)
                    os.system("tput setaf 7")


            elif ch1 == 6 :
                g = 1
                while g == 1 :
                    dockerManagement(ip_add)
                    os.system("tput setaf 7")

        os.system("tput setaf 7")
        a = int(input("For Return to main menu Press 1 and For exit Press any other number to exit: "  ))
        os.system("clear")
[root@DevOps Documents]# cat packages.py

import os
                                    # Basic Operation
def basicOperation(ip_add):
    c = 1
    while c == 1:
        os.system("tput setaf 1")
        print("""

                Press 1: For check system date
                Press 2: For System Calender
                Press 3: For Check Currently User Name
                Press 4: For Currently Working Ditectory
                Press 5: For Delete a File
                Press 6: For Delete a Directory
                Press 7: For Listing Of File
                Press 8: For Calculate Number Of Word In A File
                Press 0: For exit

        """)
        os.system("tput setaf 7")
        print("Please Enter Numebr Only")
        ch2 = int(input("Enter Your Choise : "))

        if ch2 == 1 :
            os.system("ssh {} date".format(ip_add))
        elif ch2 == 2 :
            os.system("ssh {} cal".format(ip_add))
        elif ch2 == 3 :
            os.system("ssh {} whoami".format(ip_add))
        elif ch2 == 4 :
            os.system("ssh {} pwd".format(ip_add))
        elif ch2 == 5 :
            fileName = input("Enter File name which You want to Delete With path : ")
            t = os.system("ssh {}rm -f {}".format(fileName))
            print(t)
        elif ch2 == 6 :
            dirName = input("Enter Directory Name with Path")
            os.system("ssh {} rmdir -rf {0}".format(ip_add,dirName))
        elif ch2 == 7 :
            os.system("ssh {} ls".format(ip_add))
        elif ch2 == 8 :

            fileName = input("Enter Name Of File Which You Want To Count : ")
            os.system("ssh {} cat {} | wc".format(ip_add,fileName))
        elif ch2 == 0 :
            print("""

                You exit For Current Menu

            """)
            c = 2
        else :
            print("You Enter A Worng Input")


                                    #Package Management

def packManagement(ip_add):
    d = 1
    while d == 1:
        os.system("tput setaf 1")
        print("You Select Package Management" , end = "\n\n")
        print("""

                Press 1: For Check Package Install Or Not
                Press 2: For Install Package
                Press 3: For Remove Package
                Press 0: For exit

        """)
        os.system("tput setaf 7")
        print("Please Enter Numebr Only")
        ch2 = int(input("Enter Your Choise : "))

        if ch2 == 1 :
            pack = input("Enter Package Name Which You Want To Check : ")
            os.system("ssh {} rpm -q {}".format(ip_add,pack))
        elif ch2 == 2 :
            pack = input("Enter Package Name Which You Want To Install : ")
            x = os.system("ssh {} rpm -q {}".format(ip_add,pack))
            if x != 0 :
                print("""
                    In your System {} not installed yet.
                    So we download it first and it will take some time
                """.format(pack))
                os.system("ssh {} dnf install {} -y".format(ip_add,pack))
        elif ch2 == 3 :
            pack = input("Enter Package Name Which You Want To Uninstall : ")
            x = os.system("ssh {} rpm -q {}".format(ip_add,pack))
            if x == 0 :
                print("""
                    In your System {} installed .
                    So we remove it for you and it will take some time
                """.format(pack))
                os.system("ssh {} dnf remove {} -y".format(id_add,pack))
        elif ch2 == 0 :
            print("""

                You exit For Current Menu

            """)
            d = 2
        else :
            print("You Enter A Worng Input")


                                        #Main Menu

def mainMenu(ip_add):
    os.system("tput setaf 1")
    print("""
                Press 1 : For Basic Operation
                Press 2 : For Package Management
                Press 3 : For User Management
                Press 4 : For Networking
                Press 5 : For Services Management
                Press 6 : For Use Docker
                Press 0 : exit
    """)
    os.system("tput setaf 7")
    #os.system("ssh-keygen")
    os.system("ssh-copy-id root@{}".format(ip_add))
    # print("Please Only Enter Number")
    # ch1 = int(input("Enter Your Choice : "))


                                    #UserManagement

def userManagement(ip_add):
    print("You Select User Management" , end = "\n\n")
    os.system("tput setaf 1")
    print("""

                Press 1:  For Check Current Login User
                Press 2:  For Show All User Name
                Press 3:  For Add User
                Press 4:  For Remove User
                Press 5:  For Change Password Of A User
                Press 6:  For Add Group
                Press 7:  For Remove Group
                Press 8:  For lock User
                Press 9:  For Unlock User
                Press 0:  For exit

    """)
    os.system("tput setaf 7")
    print("Please Enter Numebr Only")
    ch2 = int(input("Enter Your Choise : "))

    if ch2 == 1 :
        os.system("ssh {} whoami".format(ip_add))
    elif ch2 == 2 :
        os.system("ssh {} ls /home/".format(ip_add))
    elif ch2 == 3 :
        userName = input("Enter User Name : ")
        os.system("ssh {} useradd {}".format(ip_add,userName))
        os.system("ssh {} passwd {}".format(ip_add,userName))
        print("User added Successfuly")
    elif ch2 == 4 :
        userName = input("Enter User Name Which You want to Delete : ")
        os.system("ssh {} userdel {}".format(ip_add,userName))
        os.system("ssh {} rm -rf /home/{}".format(ip_add,serName))
        print("User Successfuly Remove")
    elif ch2 == 5 :
        userName = input("Enter User Name which you want to change : ")
        os.system("ssh {} passwd {}".format(ip_add,userName))
        print("User Password Successfuly")
    elif ch2 == 6 :
        grpName = input("Enter Group Name : ")
        os.system("ssh {} groupadd {}".format(ip_add,grpName))
        print("User added Successfuly")
    elif ch2 == 7 :
        grpName = input("Enter Group Name which You Want To Delete : ")
        os.system("ssh {} groupdel {}".format(ip_add,grpName))
        print("User Deleted Successfuly")
    elif ch2 == 8 :
        userName = input("Enter User Name Which User You Want To Lock : ")
        os.system("ssh {} usermod -l".format(ip_add))
    elif ch2 == 9 :
        userName = input("Enter User Name Which User You Want To Unlock : ")
        os.system("ssh {} usermod -u".format(ip_add))
    elif ch2 == 0 :
        print("""

            You exit For Current Menu

        """)
        e = 2
    else :
        print("You Enter A Worng Input")


                                 #Networking

def Networking(ip_add):
    print("You Select Networking " , end = "\n\n")
    os.system("tput setaf 1")
    print("""

                Press 1:  For Check IP Address
                Press 2:  For Istall HTTPD
                Press 3:  For Start Services Of Web Server
                Press 4:  For Stop Services Of Web Server
                Press 5:  For Check Status Of Web Server
                Press 0:  For exit

    """)
    os.system("tput setaf 7")

    print("Please Enter Numebr Only")
    ch2 = int(input("Enter Your Choise : "))

    if ch2 == 1 :
        os.system("ssh {} ifconfig".format(ip_add))
    elif ch2 == 2 :
        i = os.system("ssh {} rpm -q httpd".format(ip_add))
        if i != 0 :
            print("""
                In your System httpd not installed yet.
                So we download it first and it will take some time
            """)
            os.system("ssh {} dnf install httpd -y".format(ip_add))
    elif ch2 == 3 :
        os.system("ssh {} systemctl start httpd".format(ip_add))
        os.system("ssh {} systemctl stop firewalld".format(ip_add))
    elif ch2 == 4 :
        os.system("ssh {} systemctl stop httpd".format(ip_add))
    elif ch2 == 5 :
        os.system("ssh {} systemctl Status httpd".format(ip_add))
    elif ch2 == 0 :
        print("""

            You exit For Current Menu

        """)
        f = 2
    else :
        print("You Enter A Worng Input")


                                #Service Management
def serviceManagement(ip_add):
    print("You Select Services Management " , end = "\n\n")
    oa.system("tput setaf 1")
    print("""

                Press 1:  For Start Services Of Web Server
                Press 2:  For Stop Services Of Web Server
                Press 3:  For Check Status Of Web Server
                Press 4:  For Start Services Of Firewall
                Press 5:  For Stop Services Of Firewall
                Press 6:  For Check Status Of Firewall
                Press 7:  For Start Services Of Docker
                Press 8:  For Stop Services Of Docker
                Press 9:  For Check Status Of Docker
                Press 0:  For exit

    """)
    os.system("tput setaf 7")

    print("Please Enter Numebr Only")
    ch2 = int(input("Enter Your Choise : "))

    if ch2 == 1 :
        os.system("ssh {} systemctl start httpd".format(ip_add))
        os.system("ssh {} systemctl stop firewalld".format(ip_add))
    elif ch2 == 2 :
        os.system("ssh {} systemctl stop httpd".format(ip_add))
    elif ch2 == 3 :
        os.system("ssh {} systemctl status httpd".format(ip_add))
    elif ch2 == 4 :
        os.system("ssh {} systemctl start firewalld".format(ip_add))
    elif ch2 == 5 :
        os.system("ssh {} systemctl stop firewalld".format(ip_add))
    elif ch2 == 6 :
        os.system("ssh {} systemctl status firewalld".format(ip_add))
    elif ch2 == 7 :
        os.system("ssh {} systemctl start docker".format(ip_add))
    elif ch2 == 8 :
        os.system("ssh {} systemctl stop docker".format(ip_add))
    elif ch2 == 9 :
        os.system("ssh {} systemctl status docker".format(ip_add))
    elif ch2 == 0 :
        print("""

            You exit For Current Menu

        """)
        f = 2
    else :
        print("You Enter A Worng Input")



                                        # Docker Management
def dockerManagement(ip_add):
    print("You Select Docker Management " , end = "\n\n")
    os.system("tput setaf 1")
    print("""

                Press 1:   For Download Docker In Your System
                Press 2:   For Start Services Of Docker
                Press 3:   For Check Status Of Docker
                Press 4:   For Pull Docker Image
                Press 5:   For See All Docker Images In your System
                Press 6:   For Run A Docker Container
                Press 7:   For See All Currently Running Docker Container
                Press 8:   For Stop Services Of Docker
                Press 9:   For Remove Docker Container
                Press 10:  For Remove All Running Docker Container
                Press 0:   For exit

    """)
    os.system("tput setaf 7")

    print("Please Enter Numebr Only")
    ch2 = int(input("Enter Your Choise : "))

    if ch2 == 1 :
        x = os.system("ssh {} rpm -q docker-ce".format(ip_add))
        if x != 0 :

            net = os.system("ssh {} dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo".format(ip_add))
            if net != 0 :
                Print("Please Check Your Internet Connection And Try Again")
            else :
                print("It Will Take Time According To Your Internet Speed" , end = "\n\n")
                inst = os.system("ssh {} dnf install docker-ce --nobest -y".format(ip_add))
                if inst != 0 :
                    print("Some Problem Occur Please Try Agian")
                else :
                    os.system("ssh {} firewall-cmd  --permanent --zone=public --add-masquerade".format(ip_add))
                    os.system("ssh {} firewall-cmd --reload".format(ip_add))
                    os.system("ssh {} systemctl restart docker".format(ip_add))
                    print("Docker Successfully Install In Your System")


    elif ch2 == 2 :
        os.system("ssh {} systemctl start docker".format(ip_add))
    elif ch2 == 3 :
        os.system("ssh {} systemctl status docker".format(ip_add))
    elif ch2 == 4 :
        h = 1
        while h == 1:

            os.system("tput setaf 1")
            print("""

                        Press 1 : For ubuntu latest version
                        Press 2 : For centos Version 7
                        Press 3 : For Centos Latest Version
                        Press 0 : For Exit From This Menu

            """)
            os.system("tput setaf 7")
            print("Please Enter Numebr Only")
            ch3 = int(input("Enter Your Choice : "))
            if ch3 == 1:
                os.system("ssh {} docker pull ubuntu".format(ip_add))
            elif ch3 == 2:
                os.system("ssh {} docker pull centos:7".format(ip_add))
            elif ch == 2:
                os.system("ssh {} docker pull centos".format(ip_add))

            elif 0:
                print("""
                    exit from that menu
                """)
                h = 2
            else :
                print("Entereds wrong value please try again :")


    elif ch2 == 5 :
        os.system("ssh  {} systemctl stop firewalld".format(ip_add))
    elif ch2 == 6 :
        os.system("ssh {} systemctl status firewalld".format(ip_add))
    elif ch2 == 7 :
        os.system("ssh {} systemctl start docker".format(ip_add))
    elif ch2 == 8 :
        os.system("ssh {} systemctl stop docker".format(ip_add))
    elif ch2 == 9 :
        os.system("ssh {} systemctl status docker".format(ip_add))
    elif ch2 == 0 :
        print("""

            You exit For Current Menu

        """)
        f = 2
    else :
        print("You Enter A Worng Input")

def MyDetails():
        os.system("tput setaf 3")
        print("""

                        Name : Shubham Jangid
                        Course : #IIEC_RISE #Docker
                        Mobile NUmber : 9649543318
                        Email : shubhamjangid532@gmail.com
        """)
        os.system("tput setaf 7")