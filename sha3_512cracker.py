import hashlib
import sys
import os
haha = 0

sys.ps1 = '\033[91m'



print(sys.ps1)

print('''
 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
            SHA3_512 Hash cracker by V1 MoDzZz
                       
''')


passlist = input("Enter the directory of your wordlist : ")

phash = input("enter ur hash : ")



try:
    file = open (passlist, "r")

except:
    print("error: file not valid please make sure you enter correct directory")
    sys.exit()

print("bruteforcing please wait... it gonna take some time depends on password")

for pws in file:
    encoword = pws.encode('utf-8')
    dig = hashlib.sha3_512(encoword.strip()).hexdigest()
    if (dig == phash):
        print("")
        print("")
        print("")
        print(pws, " is the password")
        haha = 1
        break
        
if (haha == 0):
    print("passphrase not found")
