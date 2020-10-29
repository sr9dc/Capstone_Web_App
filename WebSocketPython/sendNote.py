import socket
import PySimpleGUI as sg
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


generate_key()


def load_key():
    return open("secret.key", "rb").read()
# UDP_IP = "127.0.0.1"
# UDP_PORT = 5004

# print("UDP target IP: %s" % UDP_IP)
# print("UDP target port: %s" % UDP_PORT)


sg.theme('DarkAmber')
layout = [[sg.Text('Capstone Demo'), sg.Text("UDP target IP:"), sg.InputText(size=(15, 15)), sg.Text("UDP target port:"), sg.InputText(size=(10,10))],
           [sg.Text("Send message:"), sg.InputText()],
           [sg.OK(), sg.Cancel()]]

window = sg.Window("Demo", layout)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event in (sg.WIN_CLOSED, 'OK'):
        UDP_IP = values.get(0)
        UDP_PORT = int(values.get(1))
        MESSAGE = values.get(2)
        MESSAGE = MESSAGE.encode()
        f = Fernet(load_key())
        encrypted_message = f.encrypt(MESSAGE)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(encrypted_message, (UDP_IP, UDP_PORT))




