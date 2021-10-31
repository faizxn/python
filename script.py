

import paramiko
import time

print("")
print("  DOT Internet (ISP) - Queue Script   ")
print("")
print("     0 : Unlimited ")
print("     1 : Peak ")
print("     2 : Off-Peak ")
print("     3 : Off-Peak-50-Percent ")
print("     4 : Special Bandwidth ")
print("")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


uttaranat = {'hostname': '59.153.100.110', 'port': '2020', 'username':'faiz', 'password':'###'}
greenroadnat = {'hostname': '59.153.100.118', 'port': '2020', 'username':'faiz', 'password':'###'}


mirpurboro = {'hostname': '59.153.100.9', 'port': '2020', 'username':'faiz', 'password':'###'}
dhakauddan = {'hostname': '59.153.100.14', 'port': '2020', 'username':'faiz', 'password':'###'}
banani = {'hostname': '59.153.100.15', 'port': '2020', 'username':'faiz', 'password':'###'}
hq = {'hostname': '59.153.100.17', 'port': '2020', 'username':'faiz', 'password':'###'}
dhanmondi = {'hostname': '59.153.100.21', 'port': '2020', 'username':'faiz', 'password':'###'}
modhubazar = {'hostname': '59.153.100.22', 'port': '2020', 'username':'faiz', 'password':'###'}
monshurabad = {'hostname': '59.153.100.24', 'port': '2020', 'username':'faiz', 'password':'###'}
bosila = {'hostname': '59.153.100.25', 'port': '2020', 'username':'faiz', 'password':'###'}
jigatola = {'hostname': '59.153.100.26', 'port': '2020', 'username':'faiz', 'password':'###'}
basundhara = {'hostname': '59.153.100.27', 'port': '2020', 'username':'faiz', 'password':'###'}
tejkunipara = {'hostname': '59.153.100.28', 'port': '2020', 'username':'faiz', 'password':'###'}
nimtola = {'hostname': '59.153.100.29', 'port': '2020', 'username':'faiz', 'password':'###'}
jamunafuturepark = {'hostname': '59.153.100.35', 'port': '2020', 'username':'faiz', 'password':'###'}
jamuna = {'hostname': '59.153.100.31', 'port': '2020', 'username':'faiz', 'password':'###'}
atibazar = {'hostname': '59.153.100.34', 'port': '2020', 'username':'faiz', 'password':'###'}
shamoly = {'hostname': '59.153.100.11', 'port': '2020', 'username':'faiz', 'password':'###'}
mohammadpur = {'hostname': '59.153.100.16', 'port': '2020', 'username':'faiz', 'password':'###'}
niknet = {'hostname': '59.153.100.12', 'port': '2020', 'username':'faiz', 'password':'###'}


routers = [ uttaranat, greenroadnat, mirpurboro, dhakauddan, banani, hq, dhanmondi, mohammadpur, modhubazar, monshurabad, bosila, jigatola, basundhara, tejkunipara, nimtola, jamunafuturepark, jamuna, atibazar, shamoly, niknet]

script_id = input("Enter Script Value : ")
    
for router in routers:

    print(f'Connected to {router["hostname"]}')
    print("")
    client.connect(**router)

    stdin, stdout, stderr = client.exec_command(f'system script run {script_id}')
    for line in stdout:
        print(line.strip('\n'))
        
client.close()



