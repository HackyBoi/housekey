import os, sys, json

prompt = ">"
	
print("housekey 0.0.1")
while True:
	command = input(prompt)
	args = command.split(' ')
	command = args[0]
	args = args[1:]
	
	if(command == "use"):
		if not(args[0]):
			print("Usage: use <driver/module> <args>")
			
		elif(args[0] == "driver"):
			#Import driver
			if not(args[2]):
				print("Usage: use driver <driver type> <driver name>")
				print("Possible driver types: SDR")
				
			if(args[1] == "SDR"):
				try:
					global SDRDriver
					SDRDriver = exec(open("drivers/" + args[2] + "/" + args[2] + ".py").read())
					
				except FileNotFoundError:
					print("File not found!")
					
				except:
					print("Unknown error!")
					
			else:
				print("Usage: use driver <driver type> <driver name>")
				print("Possible driver types: SDR")
				
		elif(args[0] == "module"):
			if not(args[1]):
				print("Usage: use module <path>")
				
			try:
				prompt = args[1] + ">"
				exec(open("modules/" + args[1] + ".py").read())
				
			except FileNotFoundError:
				print("File not found!")
				
			except:
				print("Unknown error!")
				
		else:
			print("Usage: use <driver/module> <args>")
	
