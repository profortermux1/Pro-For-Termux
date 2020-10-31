import os,sys,time
import random

os.system("clear")

os.system('git pull')

os.system("clear")

# Banner "Slow Index Logo Pro For Termux"

from V7xStyle import Style

from pyfiglet import Figlet #Animation Figlet

def render(text,style):
        	f = Figlet(font=style)
        	print(f.renderText(text))

##############################
#V7xStyle

from V7xStyle import Animation

An = Animation
#############################
#TypeWriter

def jalan(z) :
	for e in z + '\n' :
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
################################
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']

################################$

text='''              
            \033[1;31m ___                ______    
            / __ \________     / ____/__    ____ 
          / /_/ / ___/ __ \   / /_  / __ \/ ___/
        / ____/ /  / /_/ /  / __/ / /_/ / /
      /_/   /_/   \____/  /_/    \____/_/'''  
       

time.sleep(0.3)


An.SlowIndex(text,t=0.002)

time.sleep(0.3)

text2='''
   \033[1;34m______     
 /_  _ _/__  _________ ___  __  ___  __        
   / / / _ \/ ___/ __ `__ \/ / / / |/_/
  / / /  __/ /  / / / / / / /_/ />  <
 /_/  \___/_/  /_/ /_/ /_/\__,_/_/|_|'''

time.sleep(0.3)

An.SlowIndex(text2,t=0.002)

time.sleep(0.3)

print("\n")

time.sleep(0.6)
#######################################################
version='''                     

                                         \033[1;33mVerion 3.1'''
########################################################

print(version)

print('\n')

time.sleep(0.6)

S = Style('═╬════►    Pro For Termux   ',).Square()

time.sleep(0.5)

print(S)

print('\n')

jalan("\033[1;36m>>>>>>>>>>>>>>>>>>>>>>>")

print('\n')

from getpass import getpass
time.sleep(0.5)
#######################################################
textD='''

       ▄▀▀▀▄
  █    █
 ███████         ▄▀▀▄
░██─▀─██░░█▀█▀▀▀▀█░░█░      \033[1;30mpassowrd \033[1;31mcorrect!
░███▄███░░▀░▀░░░░░▀▀░░
'''
##########################################################
textP='''
 +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
 |p| |a| |s| |s| |o| |w| |r| |d| = \033[1;32mPro For Termux
 +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+'''
         
####################################################
time.sleep(0.4)
print(textP)
print('\n')
jalan("\033[1;36m>>>>>>>>>>>>>>>>>>>>>>>")
time.sleep(0.5)
print('\n')
while True :	
    
    passowd = getpass("\033[1;33m══> \033[1;34m Enter Passowrd: ")

    if passowd == "Pro For Termux" :
       print('\n')
       print(textD)
       print('\n')
       time.sleep(0.4)
       break
    else :
       print("\n")
       An.Text(AT='Passowrd Faild Try Again Please',text='',repeat=1)
       print("\n")
####################################################################
We='''



        \033[1;32mdGGGGMMb
       \033[1;30m@p~qp~~qMb--------> \033[1;36mCreated by Pro For Termux
       \033[1;34mM(@)(@) M|
       \033[1;35m@,----.JM|
      \033[1;36mJS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMM
 __|'\ .        |\dS qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--

'''
#####################################################
time.sleep(0.3)
print('\n')
while True :
    sub=input("\033[1;31mPlease Subscribe in Channel \033[1;32m[yes] \033[1;31mor \033[1;32m[no] : ")
    if sub == "yes" :
        os.system('xdg-open https://m.youtube.com/channel/UCkHzOCgII8a8KQRf68sHUxg')
        print('\n')
        jalan("\033[1;35mThanck You :)")
        os.system("clear")
        break
    elif sub == "no" :
        os.system("clear")
        break
    else :
        print('\n')
        jalan("\033[1;37mWrite \033[1;31m[yes] \033[1;37mor \033[1;31m[no]")
        print('\n')

print(We)
####################################################################
def main():
    time.sleep(0.9)
    print("\033[1;31m[1] \033[1;34mTo Start")
    print('\n')
    time.sleep(0.8)
    print("\033[1;31m[2] \033[1;34mInstall Ubuntu in termux ")
    print('\n')
    time.sleep(0.7)
    print('\033[1;31m[3] \033[1;34mInstall Metasploit Without Error')
    print('\n')
    time.sleep(0.6)
    print('\033[1;31m[4] \033[1;34mAdd Keys To Termux')
    print('\n')
    time.sleep(0.5)
    print("\033[1;31m[0] \033[1;34mTo Exit")
    print('\n')    
###################################################################
print('\n')
main()

print('\n')

time.sleep(0.4)


choose = input("==> \033[1;37mchoose an option : ")
if choose == '1' :
    print('\n')
    time.sleep(0.3)
    An.DL(text='B#Proccessing',t=0.1,width=50)
    os.system("clear")
    jalan("   Wait To install some package .....................................")
    print("\n")
    print("\n")
    jalan('\033[1;37m******************************Staring**********************************')

    print('\n')
    
    render('Update','banner3-D')
    
    os.system('dpkg --configure -a')
    
    os.system('apt update')

    print('\n')

    render('Ugrade','banner3-D')

    print('\n')

    os.system('apt upgrade')

    print('\n')

    render('Git','banner3-D')

    print('\n')

    os.system('pkg install git')

    print('\n')

    render('Python','banner3-D')

    print('\n')

    os.system('pkg install python')

    print('\n')

    render('Python2','banner3-D')

    print('\n')

    os.system('pkg install python2')

    print('\n')

    render('PHP','banner3-D')

    print('\n')

    os.system('pkg install php')

    print('\n')

    render('Wget','banner3-D')

    print('\n')

    os.system('pkg install wget')

    print('\n')

    render('Curl','banner3-D')

    print('\n')

    os.system('pkg install curl')

    print('\n')

    render('SSH','banner3-D')

    print('\n')

    os.system('pkg install ssh')

    render('OpenSSH','banner3-D')

    print('\n')

    os.system('pkg install openssh')

    print('\n')

    render('Tor','banner3-D')

    print('\n')

    os.system('pkg install tor')

    print('\n')

    render('future','banner3-D')

    print('\n')

    os.system('pkg install future')

    print('\n')

    render('ruby','banner3-D')

    print('\n')

    os.system('pkg install ruby')

    print('\n')

    render('coloroma','banner3-D')

    print('\n')

    os.system('pkg install colorama')

    print('\n')

    render('Zip','banner3-D')

    print('\n')

    os.system('pkg install zip && pkg unzip')

    print('\n')

    render('Thanck You','bubble')
    
    print('\n')
    
    time.sleep(0.6)
   
    time.sleep(0.6)   
    
    print('\033[1;33mThanck you For Usinfg Tool By!!')

    time.sleep(0.6)

    print('\n')
    S = Style('   Created By Pro For Termux    ').Square(Equal=True)
    
    print('\n')

    print(S)
    
    time.sleep(0.7)

    print('\n')

    An.Loading(AT=['|','/','-','\\'],text='\rG#exiting',t=0.2)
   
    print('\n')

    os.system("exit")

####################################################################
elif choose == '2' :
   print('\n')
   os.system("clear")
   time.sleep(0.9)
   print('\n')
   An.DL(text='R#proccessing',width=50)
   print('\n')
   time.sleep(0.7)
   jalan("\033[1;30mThis Script is created by channel ProForTermux")
   time.sleep(0.7)
   print('\n')
   An.Text(AT='Wait ......',text='')
   print('\n')
   time.sleep(0.7)
   render('Install Ubuntu','slant')
   print('\n')
   time.sleep(0.7)
   jalan("\033[1;36m<><><><><><><><><><><><><><><><><><><><>")
   print('\n')
   os.system("apt update")
   time.sleep(0.7)
   os.system("apt upgrade")
   time.sleep(0.4)
   os.system("pkg install wget")
   time.sleep(0.4)
   os.system("pkg install proot")
   time.sleep(0.4)
   os.system("termux-setup-storage")
   print('\n')
   time.sleep(0.7)
   jalan("\033[1;33m......................................")
   print('\n')
   time.sleep(0.7)
   print("Install Ubuntu Now ........")
   print('\n')
   time.sleep(0.8)
   os.system('cd /data/data/com.termux/files/home;git clone https://github.com/MFDGaming/ubuntu-in-termux;cd ubuntu-in-termux;chmod +x ubuntu.sh;bash ubuntu.sh;./startubuntu.sh')
   os.system("exit")
#########################################################
##########################$#######?#?####################
elif choose == '3' :
   os.system("clear")
   render('Metasploit Framework','slant')
   print('\n')
   print('\n')
   time.sleep(0.5)
   jalan("\033[1;35mSubscribe First in Channel Pro For Termux")
   time.sleep(0.5)
   print('\n')
   os.system('xdg-open https://m.youtube.com/channel/UCkHzOCgII8a8KQRf68sHUxg')
   time.sleep(0.6)
   os.system("clear")
   print('\n')
   time.sleep(0.6)
   i1=input("\033[1;32mDo you install Metasploit [yes] or [no] : ")
   if i1 == "yes" :       
       time.sleep(0.5)
       print('\n')
       An.Loading(AT=['|','/','-','\\'],text='\rB#Wait',t=0.2)
       print('\n')
       R=Style('\033[1;33mThis Script is created by pro for termux').Square()
       print(R) 
       print('\n')
       jalan("\033[1;30mistalling metasploit Now .................")
       print('\n')
       os.system("apt update")
       os.system("apt upgrade")
       os.system("pkg install unstable-repo")
       os.system("dpkg --configure -a")
       os.system("pkg install unstable-repo")
       os.system("pkg install metasploit -y")
       os.system("dpkg --configure -a")
       os.system("pkg install metasploit -y")
       print('\n')
       jalan("\033[1;36mInstall Successufull Write \033[1;33mmsfconsole \033[1;36mTo run Metasploit !!")
       print('\n')  
       jalan("\033[1;30m>>>>>>>>>>>>>>>>>>>>>>>")
       print('\n')
       i5=input("You Would Download Text Order To Learn How To use it \033[1;31m[yes] or \033[1;31m[no] : ")
       
       if i5 == "yes" :
           print("\n")
           jalan("\033[1;30mWait To Download milah awamir by profortermux")
           print('\n')
           jalan("\033[1;33mOpen Link The milaf awamir wait 6s ... ")
           time.sleep(0.6)
           os.system('xdg-open https://gurl.pw/kQ0c')
           print('\n')
           th="\033[1;36mThanck You"
           ce=th.center(90)
           print(ce)
           os.system("exit")
       elif i5 == "no":
           print('\n')       
           jalan("\033[1;33mByeBye :(")          	
           print('\n')
           os.system("exit")
       else :
           print('\n')
           print('Write Yes Or no')
           print('\n')
           os.system("exit")
          
   elif i1 == "no" :
       time.sleep(0.3)
       print('\n')
       jalan(" \033[1;34mYou are sure :( ")
       print('\n')
       os.system("exit")       
   else :
       print('\n')
       An.Text(AT='Write Yes To run script or No to exit ',text='',CLT='\033[1;31m',repeat=1)
       time.sleep(0.5)
       print('\n')
       jalan('\033[1;30mTry Again ...')
       time.sleep(0.5)
       print('\n')
       os.system("exit")
#######################################################
elif choose == '4' :
   os.system("clear")
   os.system("cd $HOME;rm -rif .termux;mkdir .termux;cd $HOME;cd Pro-For-Termux/.main;cp termux.properties /data/data/com.termux/files/home/.termux;cd $HOME;cd .termux;termux-reload-settings")
   print('\n')
   print("\033[1;32mKeys added Thanck You :)")
   print('\n')
   r = input("\033[1;35mif You Would Remove Keys Write \033[1;32m[Y] \033[1;35mor \033[1;32m[N] \033[1;35mTo Exit : ")
   if r == 'Y' :
      print('\n')
      os.system('cd $HOME;rm -rif .termux;termux-reload-settings')
      jalan('\033[1;36mThe Keys Was be removed')
      print('\n')
      os.system('exit')
   elif r == 'N' :
      os.system('exit')
   else :
      jalan('\033[1;34mWrite [Y] or [N]')
      print('\n')
########################################################
elif choose == '0' :
   S = Style('      Created By Pro For Termux     ').Square(Equal=True)
   print('\n')
   print(S)
   print('\n')
   print("\033[1;33m┻┳|―-∩")
   time.sleep(0.7)
   print("┳┻|　　ヽ")
   time.sleep(0.7)
   print("┻┳|　●   |")
   time.sleep(0.7)
   print("┳┻|▼) _ノ")
   time.sleep(0.7)
   print("┻┳|￣　)")
   time.sleep(0.7)
   print("┳ﾐ(￣  ／")
   time.sleep(0.7)
   print("┻┳T￣")
   time.sleep(0.7)
   print('\n')
   An.Loading(text='B#exiting',t=0.3)
   print('\n')
   os.system("exit")
###################################################################
