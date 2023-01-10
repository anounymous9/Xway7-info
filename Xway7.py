import requests
import random
import socket
import webbrowser
id_tele = ('')
token_bot = ('')

#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)
def Users():
    import random
x = ('abcdefghijklmnopqrstuvwxyz1234567890_.')
user = (''.join(random.choice(x) for i in range(4)))
def emails():
   import string
email = [
    '@gmail.com',
    '@yahoo.com',
    '@outlook.com',
    '@hotmail.com',
    '@hotmail.fr']


print(''' \033[33m
 __   __                  ______ 
 \ \ / /                 |____  |
  \ V /_      ____ _ _   _   / / 
   > <\ \ /\ / / _` | | | | / /  
  / . \\ V  V / (_| | |_| |/ /   
 /_/ \_\\_/\_/ \__,_|\__, /_/    
                      __/ |      
                     |___/       
by Saif Al-klbani   |   Insta  :  xway7
\033[37m''')

print('''
\033[31m[01]\033[36m show my ip & hostname

\033[31m[02]\033[36m Random quad username

\033[31m[03]\033[36m Random email

\033[31m[00]\033[36m about

''')
chinput = input('\033[35mselect number : \033[39m')
if chinput == '1':
    gethip()
elif chinput == '2':
    print (user)
elif chinput == '00':
    print('''
    \033[34m by Saif AL-Klbani   |  insta : Xway7
    \033[32m
     Designed this tool
          
            to gather some information
            and penetration testing
            And guess the emails
    ''')
elif chinput == '3':
    f = open('users.txt','r').readlines()
count = 0
while (count < len (f) ) :
    for i in f :
        print(i.strip() +str(random.randint(1000,99999)) + random.choice(email))
  
    count += 1
