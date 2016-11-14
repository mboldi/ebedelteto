import binascii
import sys
import time
import serial
import lcddriver
import json
import requests

port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)

def commWithServer(cardID):
     url = 'http://hugo.premontrei.hu/api/v1/cardread'

     ID = cardID[:16]

     adat = {"cardreaderId": "1", "cardId": ID}

     #adat = json.loads(adatStr)

     headers = {"Content-Type": "application/json"}

     response = requests.post(url, data = json.dumps(adat), headers=headers)

     #print '\n' + str(response.json()) + '\n'

     return response.json()

def printResToLcd(response):
     lcd.lcd_clear()
     i = 0
     for i in range(4):
          line = response['output'][i]
          if len(line) <= 20:
               lcd.lcd_message(line, i+1)
          else:
               lcd.lcd_message(line[:20], i+1)

          i += 1

     return response['status']

print(port.isOpen())
print("Com Port opened...")

#initialize the display
lcd = lcddriver.lcd()
lcd_columns = 20
lcd_rows = 4

lastRead = time.time()

while True:
     uid=port.read(16)

     if str(uid) != '' and str(uid) != '\n':
          print 'Found card with UID: ' + str(uid)[:16]
          
          #beolvasott kod elkuldese a szervernek
          response = commWithServer(str(uid))

          print printResToLcd(response)
          
          lastRead = time.time()

     time.sleep(0.1)