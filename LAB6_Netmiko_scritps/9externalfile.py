#Send device configuration using an external file
from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.2.4',
    'port': '22',
    'username': 'joran',
    'password': 'cisco',
    'secret': 'cisco',
}

# Open the configuration file and read in the commands
with open('joranextern.txt', 'r') as f:
    config_commands = f.read().splitlines()

# Establish an SSH connection to the device
with ConnectHandler(**device) as net_connect:

    # Enter enable mode on the device
    net_connect.enable()

    # Send the configuration commands to the device
    output = net_connect.send_config_set(config_commands)

# Print the output
print(output)

