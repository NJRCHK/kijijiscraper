import random
import time
import csv
import urllib.request
from urllib.request import HTTPError

lastread = 0
with open("C:/kijijiscraper/spider/lastread.txt","r") as file:
	lastread = int(file.read())
print(lastread)
for i in range(lastread, 20000000):
	try:
		url = "https://www.kijijiautos.ca/vip/" + str(i) + "/"
		x = urllib.request.urlopen(url)
		with open("C:/kijijiscraper/spider/dump/" + str(i) + ".txt", "w") as file:
			file.write(str(x.read()))
		print("url read")
	except HTTPError:
		print("invalid url")
	time.sleep(random.random()+1)
	print("reading url " + str(i+1))
	with open("C:/kijijiscraper/spiderlastread.txt","w") as file:
		file.write(str(i))