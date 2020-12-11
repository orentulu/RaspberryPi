import os
import sys
import serial
import time

holder = "09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C 09 00 2E 00 3B 3B 3B 3B 0D 3C"
#test desktop
def repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            print(substring)
            return substring
            return "break"
    return (string)

def write_log(log):
    try:
        with open(os.path.join(sys.path[0], "tag_detected.txt"), 'a') as myfile:
            myfile.write(log+"\n")
        return
    except Exception, e:
        print("Exception - write log - " + str(e))

while True:
    rfid_reader = serial.Serial('/dev/ttyACM0', 57600, 6, 'N', 1, timeout=1)
    output = rfid_reader.read(70)
    output = ''.join( [ "%02X " % ord( x ) for x in output ] ).strip()
    if (holder != ""):
        print(output)
        write_log(repeats(holder))
        rfid_reader.reset_input_buffer()
        time.sleep(5)
