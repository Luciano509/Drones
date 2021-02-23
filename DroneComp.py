# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

# Drone Mission Through the First Hoop
def firsthoop():
    sendmsg('up 45')
    sendmsg('forward 250')

# Drone Mission Through the Second Hoop
def secondhoop():
    sendmsg('go 207 0 60 75')


# Drone Mission Through the Third Hoop
def thirdhoop():
    sendmsg('curve 25 -25 0 75 50 0 75')
'''
# Drone Mission Through the Fourth Hoop
def fourthhoop():
    sendmsg('go -200 0 -60 75')
    sendmsg('forward 50')
'''

print("\nLuciano Macias")
print("Program Name: Drone Competition")
print("Date: 11.6.20")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command')
        sendmsg('takeoff', 8)

        firsthoop()
        secondhoop()
        thirdhoop()
        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
