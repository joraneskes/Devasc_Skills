from netmiko import ConnectHandler

# Device information
hostname = '172.16.2.4'
username = 'joran'
password = 'cisco'
command = 'show version'

device = {
    'device_type': 'cisco_ios',
    'host': hostname,
    'username': username,
    'password': password,
}

try:
    # Establish SSH connection
    net_connect = ConnectHandler(**device)
    print(f"Connected to {hostname}")

    # Send command and retrieve output
    output = net_connect.send_command(command)
    print(f"Command output from {hostname}:")
    print(output)

    # Perform action based on output
    if 'error' in output.lower():
        print("An error occurred.")
    else:
        print("Command executed successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close SSH connection
    net_connect.disconnect()
    print(f"Disconnected from {hostname}")

