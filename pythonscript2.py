import getpass
import telnetlib

HOST = "192.168.6.37"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_Vlan_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_Vlan_3\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
