import random
import time
import csv
import urllib.request
import re
import os
from urllib.request import HTTPError

def spider():
	with open("lastread.txt","r") as file:
		lastread = int(file.read())
	for i in range(lastread, 20000000):
		try:
			url = "https://www.kijijiautos.ca/vip/" + str(i) + "/"
			x = urllib.request.urlopen(url)
			with open(str(i) + ".txt", "w") as file:
				file.write(str(x.read()))
			print("url read... parsing")
			parse(i)
		except HTTPError:
			print("invalid url")
		time.sleep(random.random()+1)
		print("reading url " + str(i+1))
		with open("lastread.txt","w") as file:
			file.write(str(i))

def parse(f):
	f = str(f)
	time.sleep(0.5)
	with open(f + ".txt", 'r') as file:
		rawstring = file.read().replace('\n','')
			
	foreignId = re.findall(r'foreignId":"([^"]*)"', rawstring)
	make = re.findall(r',"make":"([^"]*)"', rawstring)
	model = re.findall(r',"model":"([^"]*)"',rawstring)
	year = re.findall(r',"year":"([^"]*)"',rawstring)
	price = re.findall(r',"localized":"([^"]*)"',rawstring)
	cond = re.findall(r',"key":"Condition","value":"([^"]*)"',rawstring)
	kilo = re.findall(r',"key":"Kilometres","value":"([^"]*)"',rawstring)
	kilo = kilo[0].partition('\\')
	tran = re.findall(r',"key":"Transmission","value":"([^"]*)"',rawstring)
	drive = re.findall(r',"key":"Drivetrain","value":"([^"]*)"',rawstring)
	fuel = re.findall(r',"key":"Fuel type","value":"([^"]*)"',rawstring)

	if len(foreignId) > 0:
		foreignId = str(foreignId[0])
	else:
		foreignId = "N/A"
	if len(make) > 0:
		make = str(make[0])
	else:
		make = "N/A"
	if len(model) > 0:
		model = str(model[0])
	else:
		model = "N/A"
	if len(year) > 0:
		year = str(year[0])
	else: 
		year = "N/A"
	if len(price) > 0:
		price = str(price[0])
		price = price.replace(',', '')
	else:
		price = "N/A"
	if len(cond) > 0:
		cond = str(cond[0])
	else:
		cond = "N/A"
	if len(kilo) > 0:
		kilo = kilo[0]
		kilo = kilo.replace(',','')
	else:
		kilo = "N/A"
	if len(tran) > 0:
		tran = str(tran[0])
	else:
		tran = "N/A"
	if len(drive) > 0:
		drive = str(drive[0])
	else:
		drive = "N/A"
	if len(fuel) > 0:
		fuel = str(fuel[0])
	else:
		fuel = "N/A"
	writeto = f + "," + str(foreignId) + "," + str(make) + "," + str(model) + "," + str(year) + "," + str(price) + "," + str(cond) +"," +  str(kilo) + "," + str(tran) + "," + str(drive) + "," + str(fuel)
	with open("output.csv", 'a') as csv:
		csv.write("\n" + writeto)
	os.remove(str(f) + ".txt")
	print("parsing complete")
	
def main():
	spider()

if __name__ == "__main__":
	main()
