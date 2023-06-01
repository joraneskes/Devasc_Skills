from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.16.2.4",
    port="22",
    username="joran",
    password="cisco"
    )
output=sshCli.send_command("show version")
print(output)

# Write the output to a file
with open('joran.txt', 'w') as f:
    f.write(output)
