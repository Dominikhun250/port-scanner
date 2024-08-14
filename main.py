import socket
import os
import time
from datetime import datetime
from colorama import Fore, Style, init

init()

def check_protocol(protocol):
    if protocol != "TCP" and protocol != "UDP":
        print("Select a valid protocol.")
        return
    else:
        if protocol == "TCP":
            setted_protocol = socket.SOCK_STREAM
        else:
            if protocol == "UDP":
                setted_protocol = socket.SOCK_DGRAM
    port_scanner(target_ip)

def port_scanner(target_ip):

    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d-%H-%M')
    date = formatted_time.replace('_', ' ', 1).replace('_', ' ', 2).replace('_', ' ', 3).replace(':', ' ', 4)

    directory = f"./targets/{target_ip}/{protocol}/{date}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        for port in range(1, 65536):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"{Fore.GREEN}{target_ip}:{port}{Style.RESET_ALL}")

                with open(f"{directory}/{port}.txt", "w") as file:
                    file.write(f"{target_ip}:{port}\n")
            else:
                print(f"{Fore.RED}{target_ip}:{port}{Style.RESET_ALL}")

            sock.close()

    except Exception as e:
        print(f'Error: {e}')

target_ip = input("Ip addres: ")
protocol = input("Select a scan protocol (TCP / UDP): ")
time.sleep(1)

check_protocol(protocol)
