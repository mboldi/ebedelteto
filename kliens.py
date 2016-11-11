import binascii
import sys
import time
import serial
import lcddriver
import json
import urllib2

port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)

def commWithServer(cardID):
     ID = cardID.split('\n')[0]
     data = {
          "cardreaderId": "1",
          "cardId": ID
     }

     req = urllib2.Request('http://hugo.premontrei.hu/api/v1/cardread')
     req.add_header('Content-Type', 'application/json')

     response = urllib2.urlopen(req, json.dunps(data))

     return response

def printResToLcd(response):
     i = 0
     for i in range(3):
          line = response['output'][i]
          if len(line) <= 20:
               lcd.message(line, i+1)
          else:
               lcd.message(line[0:20], i+1)

          i += 1

     return response['status']

print(port.isOpen())
print("Com Port opened...")

#initialize the display
lcd = lcddriver.lcd()
lcd_columns = 20
lcd_rows = 4

lastRead = time.time()

lcdMsg('Erintsen kartyat\n a leolvasohoz!')

while True:
     uid=port.read(16)

     if uid not '':
          print 'Found card with UID: ' + str(uid.split('\n')[0])
          
          #beolvasott kod elkuldese a szervernek
          response = commWithServer(uid)

          print printResToLcd(response)
          
          lastRead = time.time()