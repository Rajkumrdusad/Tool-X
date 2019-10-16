# Tool Name :- Tool-X
# Author :- Rajkumar dusad
# Date :- 1/11/2017
# Powered By :- Aex Software's

import os
import sys
from time import sleep

if os.path.exists("/usr/bin/yum"):
  if os.path.exists("/usr/lib/sudo"):
    systm="fedora"
    hpath=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pac="sudo yum"
  else:
    systm="fedora"
    hpath=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pac="yum"

elif os.path.exists("/usr/bin/apt"):
  if os.path.exists("/usr/lib/sudo"):
    systm="ubuntu"
    hpath=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pac="sudo apt-get"
  else:
    systm="debian"
    hpath=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pac="apt-get"

elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
  systm="termux"
  hpath=os.getenv("HOME")+"/"
  bpath="/data/data/com.termux/files/usr/bin/"
  pac="pkg"

elif os.path.exists("/usr/bin/brew"):
  systm="mac"
  hpath=os.getenv("HOME")+"/"
  bpath="/usr/bin/"
  pac="brew"

elif os.path.exists("/bin/brew"):
  systm="mac"
  hpath=os.getenv("HOME")+"/"
  bpath="/bin/"
  pac="brew"

def Aex():
	Aex=sys.exit()

def Ux():
	Ux=os.system("clear")

def Inst():
  if systm=="termux":
    print ("""\033[01;33m ===============================================
\033[01;32m|_________________ Installing __________________|
 \033[01;33m===============================================\033[00m""")
  else:
    print ("""\033[01;33m =========================================================
\033[01;32m|_______________________ Installing ______________________|
 \033[01;33m=========================================================\033[00m""")


def Nerr():
  if systm=="termux":
	Ux()
	print ('''


\033[1;33m
          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;m\033[1;91mv2.0\033[1;m


\033[1;36m ===============================================\033[1;m
\033[1;33m|           Install Best Hacking Tool           |
\033[1;36m ===============================================\033[1;m

\033[1;31m  [ + ]  \033[1;31mWe can't install Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some error.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[1;m
\033[1;36m_________________________________________________
=================================================\033[1;m
''')
  else:
	Ux()
	print ('''


\033[1;33m
               _____           _    __  __
              |_   _|__   ___ | |   \ \/ /
                | |/ _ \ / _ \| |____\  /
                | | (_) | (_) | |____/  \     
                |_|\___/ \___/|_|   /_/\_\ \033[1;31mv2.0
\033[1;m

\033[1;36m =========================================================\033[1;m
\033[1;33m|\033[1;m               \033[1;33m Install Best Hacking Tool.\033[1;m               \033[1;33m|\033[1;m
\033[1;36m =========================================================\033[1;m

\033[1;31m  [ + ]  \033[1;31mWe can't install Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some error.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[1;m
\033[1;36m___________________________________________________________
===========================================================\033[1;m
''')

def Logo():
    if systm=="termux":
        print ('''\007\033[1;33m


          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;m\033[1;91mv2.0


\033[1;36m ===============================================
\033[1;33m|           \033[1;31m Notic for You from Tool-X.         \033[1;33m|
\033[1;36m ===============================================

\033[1;33m  [ + ] \033[1;32mUse It At Your Own Risk.
\033[1;33m  [ + ] \033[1;32mNo Warranty.
\033[1;33m  [ + ] \033[1;32mUse it legal purpose only.
\033[1;33m  [ + ] \033[1;32mWe are not responsible for your actions.
\033[1;33m  [ + ] \033[1;32mDo not do things that are forbidden.

\033[1;31m If you are installing this tool.
 that means you are agree with all terms.
\033[1;36m_________________________________________________
\033[1;36m=================================================\033[00m
			''')

    else:
        print ('''


\033[1;33m
               _____           _    __  __
              |_   _|__   ___ | |   \ \/ /
                | |/ _ \ / _ \| |____\  /
                | | (_) | (_) | |____/  \     
                |_|\___/ \___/|_|   /_/\_\ \033[1;31mv2.0

\033[1;36m ==========================================================
\033[1;33m|                \033[1;32m Notic for You from Tool-X.               \033[1;33m|
\033[1;36m ==========================================================

\033[1;33m   [ + ] \033[1;32mUse It At Your Own Risk.
\033[1;33m   [ + ] \033[1;32mNo Warranty.
\033[1;33m   [ + ] \033[1;32mUse it legal purpose only.
\033[1;33m   [ + ] \033[1;32mWe are not responsible for your actions.
\033[1;33m   [ + ] \033[1;32mDo not do things that are forbidden.

\033[1;31m  If you are installing this tool.
  that means you are agree with all terms.
\033[1;36m___________________________________________________________
===========================================================\033[00m
			''')


def Sc():
    if systm=="termux":
        print ('''\007\033[1;33m


          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;m\033[1;91mv2.0


\033[1;36m ===============================================
\033[1;33m|           Install Best Hacking Tool           |
\033[1;36m ===============================================

\033[1;33m    [ + ] \033[1;32mTool-X installed successfully.
\033[1;33m    [ + ] \033[1;32mTo run Tool-X.
\033[1;33m    [ + ] \033[1;32mType Tool-X in your terminal.
\033[1;36m_________________________________________________
=================================================\033[00m
''')
    else:
        print ('''


\033[1;33m
               _____           _    __  __
              |_   _|__   ___ | |   \ \/ /
                | |/ _ \ / _ \| |____\  /
                | | (_) | (_) | |____/  \     
                |_|\___/ \___/|_|   /_/\_\ \033[1;31mv2.0

\033[1;36m =========================================================
\033[1;33m|               \033[1;33m Install Best Hacking Tool.               \033[1;33m|
\033[1;36m =========================================================

\033[1;33m     [ + ] \033[1;32mTool-X installed successfully.
\033[1;33m     [ + ] \033[1;32mTo run Tool-X.
\033[1;33m     [ + ] \033[1;32mType Tool-X in your terminal.
\033[1;36m___________________________________________________________
===========================================================\033[00m
''')


def delf():
  if os.path.exists(hpath+".Tool-X"):
    if systm=="ubuntu":
      os.system("cd .. && sudo rm -rf Tool-X")
    else:
      os.system("cd .. && rm -rf Tool-X")
    Sc()
  else:
    Nerr()

def insok():
  if os.path.exists(bpath+"Tool-X"):
    delf()
  else:
    Nerr()

def proce():
	Inst()
	print ('''\n\033[1;32mInstalling.........\033[1;m''')
	if systm=="ubuntu":
	    os.system("cd "+hpath+" && sudo rm -rf .Tool-X")
	    os.system("cd "+bpath+" && sudo rm -rf Tool-X")
	    os.system("sudo mkdir "+hpath+".Tool-X")
	    os.system("sudo cp -r .tools core modules .Tool-X.py "+hpath+".Tool-X")
	    os.system("cd "+hpath+".Tool-X/.tools && sudo chmod +x * .* *.* .*.*")
	    os.system("cd "+hpath+".Tool-X/.tools && sudo cp -v Tool-X "+bpath)
	    os.system("cd "+hpath+".Tool-X/.tools && sudo cp -v toolx "+bpath)
	    
	    print ('''\033[1;32mGiving permissiom level for enabling Tool-X execute from terminal\033[1;m''')
	    os.system("cd "+bpath+" && sudo chmod +x Tool-X")
	    os.system("cd "+bpath+" && sudo chmod +x toolx")

	    print ('''\033[1;32mGiving permission to Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+" && sudo chmod +x .Tool-X")

	    print ('''\033[1;32mGiving permission to files in Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+".Tool-X/modules && sudo chmod +x *.* .* .*.* *")

	    print ('''\033[1;32mGiving permission to Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+".Tool-X && sudo chmod +x *.* .*.* * .*")
	    Ux()
	    insok()

	else:
	    os.system("cd "+hpath+" && rm -rf .Tool-X")
	    os.system("cd "+bpath+" && rm -rf Tool-X")
	    os.system("mkdir "+hpath+".Tool-X")
	    os.system("cp -r .tools core modules .Tool-X.py "+hpath+".Tool-X")
	    os.system("cd "+hpath+".Tool-X/.tools && chmod +x * .* *.* .*.*")
	    os.system("cd "+hpath+".Tool-X/.tools && cp Tool-X "+bpath)
	    os.system("cd "+hpath+".Tool-X/.tools && cp toolx "+bpath)
	    
	    print ('''\033[1;32mGiving permissiom level for enabling Tool-X execute from terminal\033[1;m''')
	    os.system("cd "+bpath+" && chmod 777 Tool-X")
	    os.system("cd "+bpath+" && chmod 777 toolx")
	    print ('''\033[1;32mGiving permission to Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+" && chmod +x .Tool-X")

	    print ('''\033[1;32mGiving permission to files in Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+".Tool-X/modules && chmod +x *.* .*.* * .*")

	    print ('''\033[1;32mGiving permission to Tool-X directory\033[1;m''')
	    os.system("cd "+hpath+".Tool-X && chmod +x *.* .*.* * .*")
	    Ux()
	    insok()

def Toolx():
		Ux()
		Logo()
		Tool = raw_input('''\033[1;33m Do you want to install Tool-X [Y/n]> \033[00m''')
		while Tool == "Y" or Tool == "y" or Tool == "":
			Ux()
			proce()
			Toolo = raw_input("\033[1;33m Press any key to continue >>> \033[00m")
			if Toolo == "":
			   Aex()
			else:
			   Aex()
		while Tool == "n" or Tool == "N":
			Aex()
		else:
			Toolx()

def Tool_X():
	try:
		Toolx()
	except KeyboardInterrupt:
		Ux()
		Aex()
Tool_X()
