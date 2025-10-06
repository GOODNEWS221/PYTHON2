
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.27.10",
    "username": "Gosas",
    "password": "Good5471@#_",
    "port": 22
}

net_connect = ConnectHandler(**device)

net_connect.enable()

output = net_connect.send_command("show ip int br")
print(output)

commands = ["show run", "show int g3/0"]
for command in commands:
    print(net_connect.send_command(command))

net_connect.disconnect