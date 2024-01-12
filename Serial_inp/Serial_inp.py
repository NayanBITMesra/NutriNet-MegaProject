import serial.tools.list_ports
import csv

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))

portVar = "COM4"

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


with open('bpm.csv', mode='a', newline='') as csvfile:
    fieldnames = ['BPM', ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            writer.writerow({'BPM' : packet.decode('utf').rstrip('\n')})
