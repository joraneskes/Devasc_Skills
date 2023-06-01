from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.2.4',
    'port':"22",
    'username': 'joran',
    'password': 'cisco',
    'secret': 'cisco',
}

# Establish an SSH connection to the device
with ConnectHandler(**device) as net_connect:

    net_connect.enable()


    # Send the "show running-config" command and capture the output
    output = net_connect.send_command('show run')

# Write the output to a file
with open('joran_backup.txt', 'w') as f:
    f.write(output)


