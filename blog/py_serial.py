import csv
from datetime import datetime
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))

serialInst.baudrate = 9600
serialInst.port = 'COM4'
serialInst.open()


with open('bpm.csv', mode='a')as csvfile:
    fieldname =['Time', 'Value']
    while True:
        if serialInst.in_waiting:
            writer = csv.DictWriter(csvfile, fieldnames=fieldname)
            packet = serialInst.readline()
            now = datetime.now()
            dt_object1 = now.strftime("%d/%m/%Y %H:%M:%S")
            dicti = {'Time': dt_object1, 'Value': int(int(packet.decode('utf').rstrip('\n'))/2.4)}
            print(dicti)
            writer.writerow(dicti)
