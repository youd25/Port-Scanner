import socket
import time
import os
from colorama import Fore, Style

for a in range(1):
		print(">уσυɖ°°°°°°")
		time.sleep(1)
		os.system("cls" if os.name == "nt" else "clear")
		print(Fore.RED + ">ρσят ѕ¢αηηєя: ✓")
		time.sleep(1)
		print(Fore.GREEN + ">ρσят ѕ¢αηηєя: ✓")
		time.sleep(1)
		print(Fore.BLUE + ">ρσят ѕ¢αηηєя: ✓")
		time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
print(Style.RESET_ALL)

while True:
		
	while True:
		URL = input("url   : ").strip()
		if URL == " " :
			continue
		try:
			ip = socket.gethostbyname(URL)
			print(f"url   : {URL} (ip: {ip})")
			break
		except socket.gaierror:
			print("Invalid website or IP !")
	while True:
			try:
				print("-" * 7)
				PORT1 = int(input("port 1: "))
				print("-" * 7)
				PORT2 = int(input("port 2: "))
				break
			except ValueError:
				print("Enter a valid port number !")
	os.system("clear")		
	op_ports = []
	print(Fore.RED + "=" * 30)
	for port in range(PORT1, PORT2 +1):
		try:
		    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    sock.settimeout(1)
		    sock.connect((URL, port))
		    print(Fore.GREEN + f"{port} [OPEN] {socket.getservbyport(port)}")
		    op_ports.append(port)
		except:
		  	print(Fore.RED + f"{port} [CLOSE]")
	print("=" * 30)
	for w in op_ports:
	  	print(Fore.GREEN + f"{w} [OPEN PORTS]" )
	print(Style.RESET_ALL)
	input( "\n Press Enter to return to the menu> ")
	os.system("cls" if os.name == "nt" else "clear")
		


