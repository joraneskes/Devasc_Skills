print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.16.2.7",
    port="22",
    username="joran",
    password="cisco"
    )
output=sshCli.send_command("show ip interface brief")
print(output)

