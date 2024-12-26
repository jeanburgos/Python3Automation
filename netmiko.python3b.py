from netmiko import ConnectHandler

Core1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.6.40',
    'username': 'cisco',
    'password': 'cisco',
}

Core2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.6.41',
    'username': 'cisco',
    'password': 'cisco',
}

Leaf1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.6.42',
    'username': 'cisco',
    'password': 'cisco',
}

Leaf2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.6.43',
    'username': 'cisco',
    'password': 'cisco',
}

Leaf3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.6.44',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [Core1, Core2, Leaf1, Leaf2, Leaf3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
        print ("Creating VLAN " + str(n))
        config_commands = ['no vlan ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output)
    output = net_connect.send_command(
        "show ip int br"
)
    print(output)
    output = net_connect.send_command(
        "show vlan"
)
    print(output)
    net_connect.save_config()
