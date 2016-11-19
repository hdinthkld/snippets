import paramiko
import time

host_ip = 'my.host.ip-or-name'
login_username = 'username'
login_password = 'password'
enable_password = 'enable_pwd'
 
client_pre=paramiko.SSHClient()
client_pre.load_system_host_keys()
client_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_pre.connect(host_ip, username=login_username , password=login_password, look_for_keys=False, allow_agent=False)

client=client_pre.invoke_shell()
time.sleep(2)
output=client.recv(65535)
print (output.splitlines())

client.send('enable\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send(enable_password + '\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send('terminal pager 0\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send('show version\n')
time.sleep(2)
version_info = ""
output = " "

while client.recv_ready():
 output = client.recv(1)
 print (ord(output))
 version_info += output.decode('UTF-8')

print (version_info)
client.close()
client_pre.close()