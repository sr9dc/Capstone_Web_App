# Simple UI for Client to Server Communication using UDP Sockets
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


total_packet = bytearray("",'utf-8')


medication_event_packet_header = b'\x98'
total_packet.extend(medication_event_packet_header)


print('Input how many Medication Events (1-6): ')

num_medication_events_int = int(input())
num_medication_events = bytes(chr(num_medication_events_int), 'utf-8')
total_packet.extend(num_medication_events)


i = 0
# numbers 9 = \t, 10 = \n and 13 = \r
while i < (num_medication_events_int):
    print('Hour to take for medicine', str(i+1) + ": ")
    hour_to_take = bytes(chr(int(input())), 'utf-8')
    total_packet.extend(hour_to_take)


    print('Min to take for medicine', str(i+1) + ": ")
    min_to_take = bytes(chr(int(input())), 'utf-8')
    total_packet.extend(min_to_take)


    print('How many to take for medicine', str(i+1) + ": ")
    how_many_to_take = bytes(chr(int(input())), 'utf-8')
    total_packet.extend(how_many_to_take)


    print('Which compartment to take for medicine', str(i+1) + ": ")
    which_compartment_to_take = bytes(chr(int(input())), 'utf-8')
    total_packet.extend(which_compartment_to_take)


    print('Name for medicine', str(i+1) + ": ")
    name_med = input()
    total_packet.extend(bytes(chr(len(name_med)), 'utf-8'))

    name_med_byte_arr = bytearray(name_med, 'utf-8')
    while(len(name_med_byte_arr) < 30):
        name_med_byte_arr.extend(b' ')

    total_packet.extend(bytearray(name_med_byte_arr))

    i+=1








sock.sendto(total_packet, ("127.0.0.1", 5005))

































# # total_packet = bytearray(0x98,'utf-8')
# # print(total_packet)



# # print('Name of medication: ')
# # name_med = input()

# # name_med_byte_arr = bytearray(name_med, 'utf-8')
# # while(len(name_med_byte_arr) < 30):
# #     name_med_byte_arr.extend(b' ')
# # total_packet.extend(name_med_byte_arr)

# print('List your dosage number per day: ')
# dosage = input()

# dosage_arr = bytearray(dosage, 'utf-8')











