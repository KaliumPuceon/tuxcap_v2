#! /usr/bin/python3

import time
import random
import sys

sleep_time = 55
min_weight = 900
max_weight = 5700
run_probability = 0.137


def scale_data():

    value = str(random.randint(min_weight, max_weight))

    with open('/tmp/scale_reading.txt', 'w') as file:
        file.write(value+"\n")

    with open('/home/pi/testing/testlogs/scale_log.txt', 'a') as file:
        file.write(str(int(time.time()))+','+value+"\n")

    time.sleep((random.random()*3)+2)

    with open('/tmp/scale_reading.txt', 'w') as file:
        file.write("35")

    return

def write_rfid():

    string = ""
    options = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    for index in range(13):
        string =  string + random.choice(options)

 
    with open('/home/pi/testing/testlogs/rfid_log.txt', 'a') as file:
        file.write(str(int(time.time()))+','+string+"\n")

    string = string[:3]+"."+string[3:]
    print(string)

    return


def main():

    while True:


        #sys.stderr.write("guess roll\n")
        roll = random.random()

        if roll < run_probability:

            #sys.stderr.write("passed roll\n")
            
            variant = random.random()

            if variant > 0.66:
                #sys.stderr.write("double\n")
                write_rfid()
                scale_data()
            elif (variant > 0.33 and variant < 0.66):
                #sys.stderr.write("rfid\n")
                write_rfid()
            else:
                #sys.stderr.write("scale\n")
                scale_data()

        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
