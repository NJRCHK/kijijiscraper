import re
import random
import os
import time

def parse(f):
	f = str(f)
	try:
		time.sleep(0.5)
		with open("C:/kijijiscraper/scraper/dump/" + f + ".txt", 'r') as file:
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
		writeto = str(foreignId) + "," + str(make) + "," + str(model) + "," + str(year) + "," + str(price) + "," + str(cond) +"," +  str(kilo) + "," + str(tran) + "," + str(drive) + "," + str(fuel)
		with open("C:/kijijiscraper/output.csv", 'a') as csv:
			csv.write("\n" + writeto)
		os.remove("C:/kijijiscraper/scraper/dump/" + str(f) + ".txt")
	except IndexError:
		print("out of files! waiting 2 seconds...")
		time.sleep(2)