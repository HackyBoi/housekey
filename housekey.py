import os, sys, json
prompt = ">"

# Display logo
os.system("cat logo")

while True:
	# Get command
	command = input(prompt)
	args = command.split(' ')
	command = args[0]
	args = args[1:]
	
	if(command == "use"): # Load either a driver or module
		if not(args[0]):
			print("Usage: use <driver/module> <args>")
			
		elif(args[0] == "driver"):
			#Import driver
			if not(args[2]):
				print("Usage: use driver <driver name>")
			try:
				exec(open("drivers/" + args[2] + "/" + args[2] + ".py").read())
				
			except FileNotFoundError:
				print("File not found!")
				
			except:
				print("Unknown error!")
				
		elif(args[0] == "module"):
			# Import module
			if not(args[1]):
				print("Usage: use module <path>")
				
			try:
				prompt = args[1] + ">"
				exec(open("modules/" + args[1] + ".py").read())
				
			except FileNotFoundError:
				prompt = ">"
				print("File not found!")
				
			except:
				prompt = ">"
				print("Unknown error!")
				
		else:
			print("Usage: use <driver/module> <args>")
			
	elif(command == "run"):
		# Run loaded module
		if(prompt != ">"):
			runModule()
		else:
			print("You need to select a module!")
		
	elif(command == "list"):
		# List either modules or drivers
		if(args[1]):
			if(args[0] == "modules"):
				files = os.listdir("modules")
				for f in files:
					if(f.endswith(".py")):
						print(f[:-3])
			elif(args[0] == "drivers"):
				files = os.listdir("drivers")
				for f in files:
					print(f)
		else:
			print("Usage: list <modules/drivers>")
	
	elif(command == "search"):
		#Search for modules and drivers
		if(args[0]):
			files = os.listdir("modules") + os.listdir("drivers")
			for f in files:
				if(args[0] in f):
					if(f.endswith(".py")):
						print("MODULE: " + f[:-3])
					else:
						print("DRIVER: " + f)
		else:
			print("Usage: search <term>")
