import binascii
import sys
import time
import serial
import lcddriver

port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)

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

     messageArray = message.split('\n')
     lines = len(messageArray)

     i = 1
     for i in range(lines):
          if i = 4:
               line = messageArray[i]

               j = 1
               for j in range(20-len(messageArray[i])-len(time.strftime("%B %d. %H:%M"))):
                    line += ' '
                    j += 1

               line += time.strftime("%B %d. %H:%M")

               lcd.message(line, i)
          else:
               lcd.message(messageArray[i], 1)

          i += 1

def displayTime():
     if time.time()-lastTimeUpdate >= 60:
          #ido kiirasa a jobb also sarokba

def commWithServer(cardID, when):
     #valami
     menu = 'A' #A, vagy B
     #return ehet-e? (T-F)

print(port.isOpen())
print("Com Port opened...")

#initialize the display
lcd = lcddriver.lcd()
lcd_columns = 20
lcd_rows = 4

lastRead = time.time()

lcdMsg('Erintsen kartyat\n a leolvasohoz!')

wasRead = False

menu = 'C'

while True:
     uid=port.read(16)

     if checkNet() and wasNetOutage:
          # ha volt netkimaradas es visszajott, akkor az addig evok adatainak feltoltese
          #file.readlines() - beolvassa az osszes sort arraykent
          eaters = open("eaters.txt", "r")

          for eater in eaters:
               #vegigmegy a sorokon es ha nem semmi a sor, akkor feltolti az adatokat
               if eater not '':
                    eaterId = eater.split(',')[0]
                    eaterTime = eater.split(',')[1]

                    commWithServer(eaterId, eaterTime)

          eaters.close()

          #file uritese
          os.system("rm eaters.txt")

     if uid == '':
          if wasRead:
          lcdMsg('Erintsd a kartyad\n a leolvasohoz!')
          wasRead = False
     else:
          print 'Found card with UID: ' + str(uid)
          
          if checkNet():
               #beolvasott kod elkuldese a szervernek
               if commWithServer(str(uid)):
                    #ha ehet
                    lcdMsgClear('Ehet, '+ menu + ' menu\nJo etvagyat! :)', 5)
               else:
                    lcdMsgClear('Nem ehet', 5)

               wasNetOutage = False
          else:
               wasNetOutage = True



          lcdMsg('Kartya leolvasva\n' + str(uid))
          wasRead = True
          

          lastRead = time.time()