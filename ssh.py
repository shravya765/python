
import subprocess
# In the process variable, we are declaring the remote system ip address and the command to execute on the remote system
process = subprocess.Popen("ssh 192.168.50.177   hostname -i ", shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output,stderr = process.communicate()
status = process.poll()
print (output)

