Joran Eskes
Netwerken 4
Documentatie Labs

Lab 1 - PYTHON EXPERIMENTS
--------------------------
--------------------------

Op DEVASC:
----------
Installeer: 
	pip3
		sudo apt update
		sudo apt install python3-pip

	Jupyter notebook
		pip install notebook

Scripts kunnen gevonden worden via Github repository: https://github.com/KathleenHombroeks/PythonExperiments


Foutmeldingen:
	Jupyter
		geopy.geocoders
			Installeer geopy.geocoder
			pip3 install geopy

		Folium
			Installeer folium
			pip3 install folium

	VSC
		Python updaten en herstarten

	Python
		Foutmelding’ cannot import name 'soft_unicode' from 'markupsafe' ‘
		pip install markupsafe==2.0.1 


Op WINDOWS 10:
--------------
Installeer:
	Python 3.8 and PIP
	Visual Studio Code
	Jupyter Notebook
		pip install jupyterlab
 		[notice] A new release of pip available: 22.3.1 -> 23.0.1
		[notice] To update, run: C:\Users\Joran.Eskes\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
		Pip install notebook
	Python IDLE

Foutmeldingen:
	geopy.geocoders
			Installeer geopy.geocoder
			pip3 install geopy

	Folium
			Installeer folium
			pip3 install folium


Op UBUNTU
---------

Installeer VSC
	$ sudo apt update

	$ sudo apt install software-properties-common apt-transport-https

	$ wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
	$ sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
	$ sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

	$ sudo apt update
	$ sudo apt install code




Lab 4 NETWORK INFRASTRUCTURE AND TROUBLESHOOTING
------------------------------------------------
------------------------------------------------

VLAN 10, Management: 172.16.2.0/28
	4e adres voor de router
	7e adres voor de switch

VLAN 40, Data: 172.16.2.48/28

	
Ip table
	Router: G0/0/0.10  172.16.2.4
    		G0/0/0.40  172.16.2.52
    		G0/0/1     10.199.66.102 (/27)

	Switch: 172.16.2.7
	Laptop: 172.16.2.54, DG 172.16.2.52, DNS 8.8.8.8
	TFTP:	10.199.64.134

tftp files:
	switch: joran-switch
	router: joran-router

Minimale config voor TFTP te verbinden
	Router:
		G0/1 instellen
		Static route: ip route 10.199.64.128 255.255.255.224 10.199.66.100
	Switch:
		ip address 172.16.2.7 255.255.255.240
		Default gateway 172.16.2.4
		instellen Vlan 10
		Fa01 Trunk mode
		allowed Vlan 10
 

Lab 6 NETMIKO
-------------
-------------
'show running-config' werkt niet, gebruik 'show run'.

Vraag - Connect using a Python Dictionary? 
	Zelfde, ‘device’ in ‘**device’ dient als argument.

Uitleg 'BOSSCRIPT' 
	In het script wordt eerst het commando 'show version | include uptime' verzonden om de uptime van de router te controleren. Vervolgens wordt het commando 'show ip interface brief | exclude down' gebruikt om de actieve interfaces weer te geven.
	Het script controleert vervolgens de configuratie van specifieke interfaces met het commando 'show running-config interface' en past wijzigingen aan als dat nodig is met het commando 'no shutdown'.
	Daarna wordt het commando 'show ip route' gebruikt om de routing tabel weer te geven.
	Het script configureert tenslotte een loopback interface met het commando 'interface loopback' en het commando 'ip address'.
	Na het uitvoeren van de verschillende commando's wordt de configuratie opgeslagen met het commando 'save_config'.


Lab 7 YANG, NETCONFIG and RESTCONFIG
------------------------------------
------------------------------------

Part 1: Install the CSR1000v VM
-------------------------------

Installeer de CSR1000v

Zet de netwerkadapter op bridged en kies voor je eigen Wireless.
Zet je router interface Gigabithethernet 1 op dhcp.

Navigeer vanuit webbrowser naar je https://10.176.176.152/ (CSR1000V)


Part 2: Explore YANG Models
---------------------------

ieft-interface.yang zelf aanmaken in de map pyang.
Inhoud van het script van Github handmatig overschrijven met het RAW script.
Zie screenshots

Part 3: Use NETCONF to Access an IOS XE Device
----------------------------------------------

Zie screenshots

Part 4: Use RESTCONF to Access an IOS XE Device
-----------------------------------------------
Probleem bij het script:
{
 "ietf-interfaces:interface": {
 "name": "Loopback1",
 "description": "My first RESTCONF loopback",
 "type": "iana-if-type:softwareLoopback",
 "enabled": true,
 "ietf-ip:ipv4": {
 "address": [
 {
 "ip": "10.1.1.1",
 "netmask": "255.255.255.0"
 }
 ]
 },
 "ietf-ip:ipv6": {}
 }

==>415 unsuported media type
	proberen: 	te herschrijven (JSON)
			te herschrijven naar XML	
