# Simple UI for Client to Server Communication using UDP Sockets
import socket
import PySimpleGUI as sg


sg.theme('DarkAmber')
layout = [ [sg.Text('Capstone Demo'), sg.Text("UDP target IP: "), sg.InputText(size=(15,15)),  sg.Text("UDP target port: "), sg.InputText(size=(10,10))],
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

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))




