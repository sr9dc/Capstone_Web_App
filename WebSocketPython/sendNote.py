import anvil.server
import socket
import sys
import os
import re
from Crypto.Cipher import AES
from Crypto.Util import Padding
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

SMO_PACKET_TYPE_HDR     = b'\x98'
SMO_MIN_MEDICATIONS     = 1
SMO_MAX_MEDICATIONS     = 6
SMO_MIN_HOUR            = 0
SMO_MAX_HOUR            = 23
SMO_MIN_MINUTE          = 0
SMO_MAX_MINUTE          = 59
SMO_MIN_PILLS           = 1
SMO_MAX_PILLS           = 5
SMO_MIN_COMPARTMENT     = 1
SMO_MAX_COMPARTMENT     = 6
SMO_MIN_PAYLOAD_LEN     = 0
SMO_MAX_PAYLOAD_LEN     = 30
SMO_UDP_PORT            = int(os.environ.get("SMO_UDP_PORT"))

IP_REGEX = """^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"""

SMO_AES_256_KEY = bytes.fromhex(os.environ.get("SMO_AES_256_KEY"))

#connect to anvil web app ui
anvil.server.connect(os.environ.get("SMO_ANVIL_SERVER"))

#socket for sending med packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#AES 256 encryption object
cipher = AES.new(SMO_AES_256_KEY, AES.MODE_ECB)

@anvil.server.callable
def bring_back_medication_data(table):

    packet = bytearray()
    used_compartments = set()

    while True:
        n_med_events = int(len(table[0]))
        if n_med_events >= SMO_MIN_MEDICATIONS \
            and n_med_events <= SMO_MAX_MEDICATIONS:
            break

    packet.extend(SMO_PACKET_TYPE_HDR)
    packet.extend(bytes(n_med_events.to_bytes(1, sys.byteorder)))

    for i in range(n_med_events):
        while True:
            hour_to_take = table[2][i].hour
            if hour_to_take >= SMO_MIN_HOUR \
                and hour_to_take <= SMO_MAX_HOUR:
                break

        while True:
            min_to_take = table[2][i].minute
            if min_to_take >= SMO_MIN_MINUTE \
                and min_to_take <= SMO_MAX_MINUTE:
                break
        
        while True:
            how_many_to_take = int(table[1][i])
            if how_many_to_take >= SMO_MIN_PILLS \
                and how_many_to_take <= SMO_MAX_PILLS:
                break

        while True:
            which_compartment_to_take = int(table[3][i])
            if which_compartment_to_take >= SMO_MIN_COMPARTMENT \
                and which_compartment_to_take <= SMO_MAX_COMPARTMENT \
                and not which_compartment_to_take in used_compartments:
                used_compartments.add(which_compartment_to_take)
                break

        name_med = table[0][i]
        name_med_len = len(name_med)
        name_med = name_med.ljust(SMO_MAX_PAYLOAD_LEN, '\0')[:SMO_MAX_PAYLOAD_LEN]

        packet.extend(hour_to_take.to_bytes(1, sys.byteorder))
        packet.extend(min_to_take.to_bytes(1, sys.byteorder))
        packet.extend(how_many_to_take.to_bytes(1, sys.byteorder))
        packet.extend((which_compartment_to_take-1).to_bytes(1, sys.byteorder))
        packet.extend(name_med_len.to_bytes(1, sys.byteorder))
        packet.extend(bytes(name_med, "utf-8"))

    while True:
        hexip = table[4]
        ip_addr = ".".join([repr(int(s,16)) for s in hexip.split(":")])
        if (re.search(IP_REGEX, ip_addr)):
            break

    padded = Padding.pad(packet, AES.block_size)
    ciphertext = cipher.encrypt(padded)
    res = sock.sendto(ciphertext, (ip_addr, SMO_UDP_PORT))

    if res > 0:
        print("Sent %d bytes to %s" % (res, ip_addr))
    else:
        print("Error sending to %s" % (ip_addr))

anvil.server.wait_forever()
