#!/usr/bin/env python3.11
# dpw@plaza.localdomain
# 2024-01-16 18:35:28

import sys
import serial

serial_port = '/dev/tty.usbmodemF412FA649B242';
baud_rate = 19200;

def main(args) -> None:
    # print(f'{args}')
    ser = serial.Serial(serial_port, baud_rate)
    print("open? ", ser.is_open);

    # response = ser.readline().decode('utf-8').strip();
    # print("response: ", response);

    ser.write(b'Hello arduino board.\n');
    response = ser.readline().decode('utf-8').strip();
    print("response: ", response);

    ser.close();

if __name__ == '__main__':
    main(sys.argv[1:])

