from netmiko import ConnectHandler
from multiprocessing import Pool

# Define the device parameters for each device
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "172.16.2.4",
        "username": "joran",
        "password": "cisco",
        "secret": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "ip": "172.16.2.7",
        "username": "joran",
        "password": "cisco",
        "secret": "cisco",
    },
]

# Define the show commands
show_commands = ["show version", "show run | incl hostname"]

# Define a worker function to execute the commands on each device
def worker(device):
    with ConnectHandler(**device) as net_connect:
        output = ""
        for command in show_commands:
            output += f"\n{device['ip']}: {command}\n"
            output += net_connect.send_command(command)
        return output

# Use a process pool to execute the worker function concurrently on each device
with Pool(len(devices)) as pool:
    results = pool.map(worker, devices)

# Print the results
for result in results:
    print(result)
