import paramiko

def ssh_command(hostname,user,password):

    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname,'22',user,password,timeout=5)
        commands = ['vmstat','uname -a','df -h']
        for command in commands:
            try:
                stdin,stdout,stderr = s.exec_command(command,timeout=5,get_pty=True)
                print(stdout.read())
            except Exception as e:
                print(hostname + ":" + command + ' timeout!')
        s.close
    except:
        print("Sorry, the host " + hostname + " does not online.")

filename = 'client.txt'
try:
	with open(filename) as file_object:
		for a in file_object:
			ssh_command(a.rstrip())
except FileNotFoundError:
	print("Sorry, the file " + filename + " does not exist.")
