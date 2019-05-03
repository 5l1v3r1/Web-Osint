try:
	import socket
	import requests
	import dns.resolver
	import Air_Ng as air
	from colorama import Fore, Back, Style
	import os
	import sys
	import time
except ImportError as ie:
	print("[-]Missing Modules")

os.system("clear")

print(Style.BRIGHT + """
	#=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-#
	-  Access information Reconnaissance - Network Gathering  -
	=	Follow Me On Github ==> hacker900123		  =
	#		 More Features Soon			  #
	-	Sit Back And Watch It Do Its Reconnaissance	  -
	=		 Use It Responsibly			  =
	#=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-=#-#
""")


print(Fore.CYAN + ">> [*] Script Initializing.....")
time.sleep(3)
print(Fore.GREEN + ">> [+] Script Initialized Successfully!")
website = input(Fore.BLUE + ">> [?] Enter Website To Recon: ")
print(Fore.CYAN + ">> [*] Scanning For Geo Ip Info....")
time.sleep(2)
Ip = socket.gethostbyname(website)
geo_Ip = air.geoIplookup(website)
geo_Country = geo_Ip.country
geo_City = geo_Ip.city
geo_Country_Code = geo_Ip.countryCode
geo_Host = geo_Ip.host
geo_info_Name = geo_Ip.info_name
geo_Isp = geo_Ip.isp
geo_lat = geo_Ip.lat
geo_long = geo_Ip.lon
geo_org = geo_Ip.org
geo_region = geo_Ip.region
geo_region_Name = geo_Ip.regionName
geo_Status = geo_Ip.status
geo_Time_Zone = geo_Ip.timezone
geo_zip = geo_Ip.zip
print(Fore.GREEN + ">> [+] Geo Ip Info Found!")
time.sleep(2)
print(Fore.YELLOW + ">> [+] Server Ip: " + Ip)
print(Fore.YELLOW + ">> [+] Country: " + geo_Country)
time.sleep(1)
print(Fore.YELLOW + ">> [+] City: " + geo_City)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Country Code: " + geo_Country_Code)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Host: " + geo_Host)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Info Name: " + geo_info_Name)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Isp: " + geo_Isp)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Latitude: " + str(geo_lat))
time.sleep(1)
print(Fore.YELLOW + ">> [+] Longitude: " + str(geo_long))
time.sleep(1)
print(Fore.YELLOW + ">> [+] Organization: " + geo_org)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Region: " + geo_region)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Region Name: " + geo_region_Name)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Satuts: " + geo_Status)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Time Zone: " + geo_Time_Zone)
time.sleep(1)
print(Fore.YELLOW + ">> [+] Zip: " + geo_zip)

print(Fore.CYAN + ">> [*] Running A Reverse Ip Lookup....")
x = air.reverseIplookup(website)
list_Ip = x.show_list_Ip
arr = []
arr.append(list_Ip)
time.sleep(3)
print(Fore.CYAN + ">> [*] Extracting Reverse Domains Found....")
time.sleep(3)
for ip in list_Ip:
	time.sleep(1)
	print(Fore.YELLOW + ">> [+] " + ip)

print(Fore.CYAN + ">> [*] Running A Name Server Detection....")
nameservers = dns.resolver.query(website,'NS')
time.sleep(2)
print(Fore.CYAN + ">> [*] Extracting Name Servers....")
time.sleep(4)
for data in nameservers:
		time.sleep(1)
		print (Fore.GREEN + ">> [+] " + str(data))

print(Fore.CYAN + ">> [*] Running A Subdomain Scan....")
subdomains = air.subdomainSearcher(website)
l = subdomains.list
arrayy = []
arrayy.append(l)
time.sleep(2)
print(Fore.CYAN + ">> [*] Extracting Subdomains....")
for sub in l:
	time.sleep(1)
	print(Fore.YELLOW + ">> [+] Subdomain: " + str(sub))

print(Fore.CYAN + ">> [*] Running Server And Encoding Type Detection....")

add_Http = "http://"
full_Url = add_Http + website

request = requests.get(full_Url)

server = request.headers['server']
encoding = request.headers['content-type']

time.sleep(2)

print(Fore.CYAN + ">> [*] Extracting Info....")
time.sleep(3)

print(Fore.YELLOW + ">> [+] Server: " + server)
print(Fore.YELLOW + ">> [+] Encoding: " + encoding)

try:
	print(Fore.CYAN + ">> [*] Running Time Of Website Creation And Expiration Detection....")
	who_Is = air.whoisLookup(website)
	all = (who_Is.show_data)
	print(Fore.CYAN + ">> [*] Extracting Info... ")
	time.sleep(4)
	creation = (all['creation_date'])
	expiration = (all['expiration_date'])
	if(creation == None):
		print(Fore.RED + ">> [-] Creation Date Could Not Be Found Or Retrieved!")
	if(expiration == None):
		print(Fore.RED + ">> [-] Expiration Date Could Not Be Found Or Retrieved!")
	else:
		print(Fore.YELLOW + ">> [+] Website Created At " + str(creation))
		time.sleep(2)
		print(Fore.YELLOW + ">> [+] Website Will Expire At " + str(expiration))
		time.sleep(2)
except Exception as e:
	print(e)

print(Fore.CYAN + ">> [*] Running Registrar And Last Modified Detection...")

who_Iss = air.whoisLookup(website)
alll = (who_Iss.show_data)

print(Fore.CYAN + ">> [*] Extracting Info....")
time.sleep(4)
Registrar = (alll['registrar'])
print(Fore.YELLOW + ">> [+] Registrar: " + str(Registrar))
time.sleep(4)
last_Modified = (all['updated_date'])
print(Fore.CYAN + ">> [+] Extracting Last Modification Date...")
time.sleep(3)
aa = []
aa.append(last_Modified)
for i in aa:
	print(Fore.YELLOW + ">> [+] Last Modified In " + str(i))
	break

print(Fore.CYAN + ">> [*] Running Organization And Address Detection....")
whoo_Is = air.whoisLookup(website)
al = (whoo_Is.show_data)
print(Fore.CYAN + ">> [*] Extracting Info.....")
time.sleep(4)
who_is_server = (al['whois_server'])
print(Fore.YELLOW + ">> [+] Whois Server: " + str(who_is_server))
time.sleep(3)
name = (al['name'])
print(Fore.YELLOW + ">> [+] Name: " + str(name))
time.sleep(3)
org =  (al['org'])
print(Fore.YELLOW + ">> [+] Organization: " + str(org))
time.sleep(3)
address = (al['address'])
print(Fore.YELLOW + ">> [+] Address: " + str(address))
time.sleep(2)
city = (al['city'])
print(Fore.YELLOW + ">> [+] City: " + str(city))
time.sleep(2)
state = (al['state'])
print(Fore.YELLOW + ">> [+] State: " + str(state))
time.sleep(2)
zipcode = (al['zipcode'])
print(Fore.YELLOW + ">> [+] ZipCode: " + str(zipcode))
time.sleep(2)
country = (al['country'])
print(Fore.YELLOW + ">> [+] Country: " + str(country))


print(Fore.CYAN + ">> [*] Running Email Extraction....")
time.sleep(2)
emails = air.emailExtractor(full_Url)
listt = emails.search
print(Fore.CYAN + ">> [*] Extracting Emails....")
time.sleep(3)
for email in listt:
	print(Fore.YELLOW + ">> [+] Email: " + str(email))
 
