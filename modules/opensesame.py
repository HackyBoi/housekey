'''
	TODO:
	- De bruijn
	- Send Codes
	- Other stuff
'''

class GarageKey:
	def __init__(self, hz, baud, bits, length, tri, b0, b1, b2):
		self.hz = hz
		self.baud = baud
		self.bits = bits
		self.length = length
		self.tri = tri
		self.b0 = b0
		self.b1 = b1
		self.b2 = b2

key1 = GarageKey(310000000, 2000,   10,   4,   0, 0x8, 0xe, 0x0)
key2 = GarageKey(390000000, 2000,    9,   4,   0, 0x8, 0xe, 0x0)
key3 = GarageKey(315000000, 2000,    9,   4,   0, 0x8, 0xe, 0x0)
key4 = GarageKey(318000000, 2000,    9,  18,   1, 0x020100, 0x03fd00, 0x03fdfe)
prompt = "OpenSesame >"

def mainMenu():
	print("OpenSesame - NOTE: Incomplete!")
	for key in range(len(garages)):
		print(str(key) + ". Hz: " + str(garages[key].hz) + " Baudrate: " + str(garages[key].baud) + " Bits: " + str(garages[key].bits) + " Length: " + str(garages[key].length))
	print(str(len(garages) + 1) + ". Not listed")
	selection = int(input(prompt))
	if(selection > len(garages)):
		hz = int(input("Hz? "))
		baud = int(input("Baud? "))
		bits = int(input("Bits? "))
		length = int(input("Len? "))
		tri = int(input("Tri? "))
		b0 = int(input("b0? "))
		b1 = int(input("b1? "))
		b2 = int(input("b2? "))
	else:
		hz = garages[selection].hz
		baud = garages[selection].baud
		bits = garages[selection].bits
		length= garages[selection].length
		tri = garages[selection].tri
		b0 = garages[selection].b0
		b1 = garages[selection].b1
		b2 = garages[selection].b2

garages = [key1, key2, key3, key4]
mainMenu()
