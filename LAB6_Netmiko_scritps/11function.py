from netmiko import ConnectHandler

def show_command(hostname, username, password, command):
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

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close SSH connection
        net_connect.disconnect()
        print(f"Disconnected from {hostname}")


# Example usage
hostname = '172.16.2.4'
username = 'joran'
password = 'cisco'
command = 'show version'

show_command(hostname, username, password, command)

