import socket
import sys

print('''
help: 
portscan.py 1 2 3

1. ip address
2. start range of scan
3. end ragne of scan \n''')


ip = sys.argv[1]
ps = sys.argv[2]
pe = sys.argv[3]

ps = int(ps)
pe = int(pe)

pe = pe+1

for port in range(ps,pe):
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    check = con.connect_ex((ip,port))
    if check == 0:
        print("[+] ",port," is open.")
        con.close()
    else:
        con.close()
        pass

#Created By AMIRX
