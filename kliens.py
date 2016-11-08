import binascii
import sys
import time
import serial

port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)

print(port.isOpen())
print("Com Port opened...")

#initialize the display

def checkNet():
     #check if there is internet connection
     #if there is, return True, else return False

def lcdMsgClear(message, duration):
     #lcd parancsokat atnezni!!!!!!!
     lcdMsg(message)

     time.sleep(duration)
     lcd.clear()

def lcdMsg(message):
     #lcd parancsokat atnezni!!!!!!!
     lcd.clear()

     lcd.message(message)

     if '\n' not in message:
         case = len(message) > lcd_columns
     else:
          case =  len(message.split('\n')[0]) > lcd_columns or len(message.split('\n')[1]) > lcd_columns
     
     if case:
          for i in range(len(message)-lcd_columns):
          time.sleep(0.3)
          lcd.move_left()

def commWithServer(cardID):
     menu = 'A' #A, vagy B
     #return ehet-e? (T-F)

lastRead = time.time()

lcdMsg('Erintsen kartyat\n a leolvasohoz!')

wasRead = False

menu = 'C'

while True:
     uid=port.read(16)

     if uid == '':
          if wasRead:
          lcdMsg('Erintsen kartyat\n a leolvasohoz!')
          wasRead = False
	if(time.time()-lastRead) > 60: 
          lcdMsg('Erintsen kartyat\n a leolvasohoz!')
     else:
          print 'Found card with UID: ' + str(uid)
          
          if checkNet():
               #beolvasott kod elkuldese a szervernek
               if commWithServer(str(uid)):
                    #ha ehet
                    lcdMsgClear('Ehet, '+ menu + ' menu', 5)
               else:
                    lcdMsgClear('Sajnos nem ehetsz', 5)



          lcdMsg('Kartya leolvasva\n' + str(uid))
          wasRead = True
          

          lastRead = time.time()

	#kommunikacio a szerverrel

	