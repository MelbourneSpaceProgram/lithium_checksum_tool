def validByteHexString(theString):
    if isinstance(theString, str) and len(theString) == 4 and theString[0:2] == "0x":
        return True
    else:
        return False


commandType = " "
while not validByteHexString(commandType):
    commandType = input("""Enter a command type\n 0x01 : No-Op\n 0x02 : Reset\n 0x03 : Transmit 
    \n 0x05 : Get Configuration \n 0x06 : Set Configuration \n 0x07 : Query Telemetry \n 0x08 : Write Flash 
    \n 0x09 : RF Configure \n 0x10 : Set Beacon Data \n 0x11 : Configure Beacon \n 0x12 : Read firmware rev 
    \n 0x13 : Write DIO key \n 0x14 : Firmware Update \n 0x15 : Firmware Packet\n""")

    if not validByteHexString(commandType):
        print("Invalid Input")

direction = " "
while not validByteHexString(direction):
    direction = input("Enter direction In : (0x10), Out : (0x20): ")

userInput = " "
payloadArray = []
while userInput.upper() != "DONE":
    userInput = input("Enter a 4 digit hex char (0x--), type DONE to calculate checksum\n")
    if validByteHexString(userInput):
        payloadArray.append(userInput)
    elif userInput.upper() == "DONE":
        break
    else:
        userInput = " "
        print("Invalid input")

syncCharA = 0x48 #H
syncCharB = 0x65 #e
lithiumMessage = bytearray()
lithiumMessage.append(syncCharA)
lithiumMessage.append(syncCharB)
lithiumMessage.append(bytearray.fromhex(direction[2:])[0])
lithiumMessage.append(bytearray.fromhex(commandType[2:])[0])

sizeBytes = bytearray.fromhex(format(len(payloadArray), '04x'))
for byte in sizeBytes:
    lithiumMessage.append(byte)    

for hexStr in payloadArray:
    lithiumMessage.append(bytearray.fromhex(hexStr[2:])[0])

print("Input is:" + str(lithiumMessage))

ckA = 0
ckB = 0
for i in range(2, len(lithiumMessage)):
    ckA = ckA + int(lithiumMessage[i])
    ckB = ckB + ckA

ckA %= 256
ckB %= 256

print("Checksum A: {:02X}".format(ckA))
print("Checksum B: {:02X}".format(ckB))