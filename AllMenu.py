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