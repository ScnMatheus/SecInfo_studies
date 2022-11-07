import paramiko

host= '127.0.0.1'
user = 'teste'
passwd = 'teste'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPoliciy())
client.connect(host, username=user, password=passwd)
print (client.exec_command('ls'))

while True:
    comando = raw_input('comamand: ')
    entrada, saida, erros = client.exec_command(comando)
    print (saida.readlines())