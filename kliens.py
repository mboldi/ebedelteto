import sys
import time
import serial
import lcddriver
import json
import requests

port =serial.Serial(
    port="/dev/ttyUSB0",
    #port="/dev/ttyAMA0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)

def commWithServer(cardID):
     url = 'https://hugo.premontrei.hu/api/v1/cardread'

     ID = cardID[:16]

     adat = {"cardreaderId": "1", "cardId": ID}

     headers = {"Content-Type": "application/json"}

     response = requests.post(url, data = json.dumps(adat), headers=headers)

     #print '\n' + str(response.json()) + '\n'

     return response.json()

def printResToLcd(response):
     lcd.clear()
     i = 0
     for i in range(4):
          line = response['output'][i]
          if len(line) <= 20:
               lcd.message(line, i+1)
          else:
               lcd.message(line[:20], i+1)

          i += 1

     return response['status']

def lcd_right(msg, line):
     if len(msg):
          pass

print(port.isOpen())
print("Com Port opened...")

#initialize the display
lcd = lcddriver.lcd()
lcd_columns = 20
lcd_rows = 4

lastRead = time.time()-20

wasprint = False

while True:
     uid=port.read(16)

     if str(uid) != '' and str(uid) != '\n' and len(str(uid)) > 15:
          print 'Found card with UID: ' + str(uid)[:16]
          
          #beolvasott kod elkuldese a szervernek
          response = commWithServer(str(uid))

          print printResToLcd(response)
          
          wasprint = False
          lastRead = time.time()

     if time.time()-lastRead >= 5 and not wasprint:
          lcd.clear()
          lcd.message("Erintsd a kartyat", 1)
          lcd.message("      a leolvasohoz!",2)
          wasprint = True

     time.sleep(0.1)