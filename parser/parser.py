import re
import random
import os

file = random.choice(os.listdir("C:/kijijiscraper/spider/dump"))
print("opening file: " + file)
with open("C:/Users/Nathaniel/Desktop/test/14570614.txt", 'r') as file:
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
writeto = str(foreignId[0]) + "," + str(make[0]) + "," + str(model[0]) + "," + str(year[0]) + "," + str(price[0]) + "," + str(cond[0]) +"," +  str(kilo[0]) + "," + str(tran[0]) + "," + str(drive[0]) + "," + str(fuel[0])

with open("C:/kijijiscraper/output.csv", 'a') as csv:
	csv.write("\n" + writeto)
