#!/usr/bin/env python

import sys
import socket
import json
import ctypes

class PlatoVectorParcelHeader(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('token', ctypes.c_uint32),
        ('data_size', ctypes.c_uint32),
        ('timestamp', ctypes.c_int64),
        ('fifo_id', ctypes.c_uint32),
        ('sequence_number', ctypes.c_uint32),
        ('object_id', ctypes.c_uint64),
        ('_size', ctypes.c_uint32),
        ('_element_size', ctypes.c_uint32),
        ('padding', ctypes.c_uint32 * 6)
    ]
# Hardcoded server address, change if needed
server_addr = ('127.0.0.1', 9009)

def main():
    print('Starting TCP connection to Helius...')
    # create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect the socket to the address & port
    sock.connect(server_addr)
    # receive data on this connection
    print("Connected!")
    try:
        # send a subscription string for JSON objects
        subscription = 'ojsn 1'
        print("Sending subscription:", subscription)
        sock.sendall(bytes(subscription, 'utf-8'))
        # message counter
        count = 0
        while (count < 100):
            payload = sock.recv(65535)
            print("Message count: "+ str(count))
            objects = payload[ctypes.sizeof(PlatoVectorParcelHeader):]
            print("Got objects")
            print(objects)
            count = count + 1

    finally:
        print('Closing the connection...')
        sock.close()


if __name__ == '__main__':
    main()