#Send show commands to multiple devices
from netmiko import ConnectHandler

#Define the device parameters
devices = [
{
    'device_type': 'cisco_ios',
    'host':   '172.16.2.4',
    'username': 'joran',
    'password': 'cisco',
    'port' : 22,          
    'secret': 'cisco',
},
{
    'device_type': 'cisco_ios',
    'host':   '172.16.2.7',
    'username': 'joran',
    'password': 'cisco',
    'port' : 22,          
    'secret': 'cisco',
},
]

# Define the list of show commands
commands = [
    'exit',
    'show version', 
    ]

# Iterate over devices
for device in devices:
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)
    connection.enable()

    # Execute the show commands
    output = connection.send_config_set(commands)

    # Print the output
    print(f"Device: {device['host']}")
    print(output)

    # Close the SSH connection
    connection.disconnect()
