import socket
import sys
import re

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
SMO_UDP_PORT            = 5004

IP_REGEX = """^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"""

packet = bytearray()
used_compartments = set()

while True:
    print("How many medications (%d-%d): " \
        % (SMO_MIN_MEDICATIONS, SMO_MAX_MEDICATIONS), end='')
    n_med_events = int(input())
    if n_med_events >= SMO_MIN_MEDICATIONS \
        and n_med_events <= SMO_MAX_MEDICATIONS:
        break

packet.extend(SMO_PACKET_TYPE_HDR)
packet.extend(bytes(n_med_events.to_bytes(1, sys.byteorder)))

for i in range(n_med_events):

    while True:
        print("Hour to take medication", i+1, "(%d-%d): " \
            % (SMO_MIN_HOUR, SMO_MAX_HOUR), end='')
        hour_to_take = int(input())
        if hour_to_take >= SMO_MIN_HOUR \
            and hour_to_take <= SMO_MAX_HOUR:
            break

    while True:
        print("Minute to take medication", i+1, "(%d-%d): " \
            % (SMO_MIN_MINUTE, SMO_MAX_MINUTE), end='')
        min_to_take = int(input())
        if min_to_take >= SMO_MIN_MINUTE \
            and min_to_take <= SMO_MAX_MINUTE:
            break

    while True:
        print("How many to take of medication", i+1, "(%d-%d): " \
            % (SMO_MIN_PILLS, SMO_MAX_PILLS), end='')
        how_many_to_take = int(input())
        if how_many_to_take >= SMO_MIN_PILLS \
            and how_many_to_take <= SMO_MAX_PILLS:
            break

    while True:
        print("Which compartment for medication", i+1, "(%d-%d): " \
            % (SMO_MIN_COMPARTMENT, SMO_MAX_COMPARTMENT), end='')
        which_compartment_to_take = int(input())
        if which_compartment_to_take >= SMO_MIN_COMPARTMENT \
            and which_compartment_to_take <= SMO_MAX_COMPARTMENT \
            and not which_compartment_to_take in used_compartments:
            used_compartments.add(which_compartment_to_take)
            break
        
    print("Name of medication", i+1, "(%d-%d): " \
        % (SMO_MIN_PAYLOAD_LEN, SMO_MAX_PAYLOAD_LEN), end='')
    name_med = input()
    name_med_len = len(name_med)
    name_med = name_med.ljust(SMO_MAX_PAYLOAD_LEN, '\0')[0:SMO_MAX_PAYLOAD_LEN]

    packet.extend(hour_to_take.to_bytes(1, sys.byteorder))
    packet.extend(min_to_take.to_bytes(1, sys.byteorder))
    packet.extend(how_many_to_take.to_bytes(1, sys.byteorder))
    packet.extend((which_compartment_to_take-1).to_bytes(1, sys.byteorder))
    packet.extend(name_med_len.to_bytes(1, sys.byteorder))
    packet.extend(bytes(name_med, "utf-8"))

print("Packet to send:", packet.hex())

while True:
    print("IP Address to send to: ", end='')
    ip_addr = input()
    if (re.search(IP_REGEX, ip_addr)):
        break

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
res = sock.sendto(packet, (ip_addr, SMO_UDP_PORT))

if res > 0:
    print("Sent %d bytes to %s" % (res, ip_addr))
else:
    print("Error sending to %s" % (ip_addr))
