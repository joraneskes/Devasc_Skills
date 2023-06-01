from netmiko import ConnectHandler

# Define the device information
device = {
    'device_type': 'cisco_ios',
    'ip': '172.16.2.4',
    'port':'22',
    'username': 'joran',
    'password': 'cisco',
}

# Connect to the device
with ConnectHandler(**device) as net_connect:

    # Send a command to check the uptime of the router
    output = net_connect.send_command('show version | include uptime')
    print(f"Uptime of the router: {output}")

    # Send a command to check the interface status
    output = net_connect.send_command('show ip interface brief | exclude down')
    print(f"Active interfaces: {output}")

    # Check the interface configuration and apply changes if required
    interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3']
    for interface in interfaces:
        output = net_connect.send_command(f'show running-config interface {interface}')
        if 'shutdown' in output:
            net_connect.send_config_set([f'interface {interface}', 'no shutdown'])
            print(f"Interface {interface} has been enabled")
        else:
            print(f"Interface {interface} is already enabled")

    # Send a command to check the routing table
    output = net_connect.send_command('show ip route')
    print(f"Routing table: {output}")

    # Configure a loopback interface
    loopback_number = '100'
    output = net_connect.send_config_set([f'interface loopback {loopback_number}', 'ip address 10.0.0.1 255.255.255.0'])
    print(f"Loopback interface {loopback_number} has been created")

    # Save the configuration
    output = net_connect.save_config()
    print(f"Configuration saved successfully")

