import random
import time
import urllib.request
from urllib.request import HTTPError

for i in range(14570000, 20000000):
	try:
		url = "https://www.kijijiautos.ca/vip/" + str(i) + "/"
		x = urllib.request.urlopen(url)
		with open("dump/" + str(i) + ".txt", "w") as file:
			file.write(str(x.read()))
		print("url read")
	except HTTPError:
		print("invalid url")
	time.sleep(random.random()+1)
	print("reading url " + str(i+1))