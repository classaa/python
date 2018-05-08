import psutil
#from subprocess import PIPE

#memory
a = psutil.virtual_memory()
print(a)

#cpu
b = psutil.cpu_times()
b1 = psutil.cpu_count(logical=False)
print(b,"\n",b1)

#disk
c = psutil.disk_partitions()#sdiskpart(mountpoint)
for i in c:
    print(i)

d = psutil.disk_io_counters()
print(d)

#net
e = psutil.net_io_counters()
print(e)

f = psutil.pids()
print(len(f))

g = psutil.Popen(["python","-c","print('hello')"])
#g.name()
print(g)
#g.communicate()
#g.cpu_times()
