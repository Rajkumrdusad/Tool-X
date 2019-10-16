# Tool Name :- Tool-X v2.0
# Author :- Rajkumar Dusad
# Date :- 1/10/2018
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from logo import *
from core.system import *
from time import sleep
from ins import tmn
from tos import tos
from cat import cate

def all():
  ux()
  all_logo()
  Tool = raw_input('''\n\033[1;36m ##> \033[00m''')
  if Tool == "1":
    ux()
    ins_logo()
    os.system("cd .tools && python2 .all.aex")
    ux()
    as_logo()
    Toolo = raw_input("\n\033[1;33m >>> \033[00m")
    if Toolo == "":
      pass
    else:
      pass
  elif Tool == "0":
    pass
  else:
    print ("\033[01;34m\007\n error : \033[01;37m\'"+Tool+"\' \033[01;31minvalid option !!!")
    sleep(1)
    all()

def Done():
  if system=="ubuntu":
    os.system("cd "+home+"Tool-X && sudo sh install.aex")
  else:
    os.system("cd "+home+"Tool-X && sh install.aex")
  ux()
  ups_logo()
  Toolo = raw_input("\n\033[1;33m >>> \033[00m")
  if Toolo == "":
    os.system("Tool-X")
    ex()
  else:
    os.system("Tool-X")
    ex()

def proce2():
  if os.path.exists(home+"Tool-X/install.aex"):
    Done()
  else:
    ux()
    unrr()
    tmp= raw_input("\n\033[1;33m Press any key to continue >>> \033[00m")

def proce1():
  if os.path.exists(home+"Tool-X"):
    proce2()
  else:
    ux()
    unrr()
    tmp = raw_input("\n\033[1;33m Press any key to continue >>> \033[00m")

def proce():
	print ('''\n\033[1;32mUpdating.........\033[1;m\n''')
	if system=="termux":
	  os.system("cd "+home+" && git clone https://github.com/Rajkumrdusad/Tool-X.git")
	  proce1()
	  ux()
	elif system=="debian":
	  os.system("cd "+home+" && git clone https://github.com/Rajkumrdusad/Tool-X.git")
	  proce1()
	  ux()
	else:
	  os.system("cd "+home+" && sudo git clone https://github.com/Rajkumrdusad/Tool-X.git")
	  proce1()
	  ux()

def Upt():
  ux()
  up_logo()
  Tool = raw_input('''\n\033[1;36m ##> \033[00m''')
  if Tool == "1":
    ux()
    upp_logo()
    proce()
  elif Tool == "0":
    pass
  else:
    print ("\033[01;34m\007\n error : \033[01;37m\'"+Tool+"\' \033[01;31minvalid option !!!")
    sleep(1)
    Upt()

def about():
  ux()
  a_logo()
  a=raw_input('''\n\033[1;33m >>> \033[00m''')

def term():
  while True:
    ux()
    menu()
    Tool = raw_input('''\033[1;36m
 ##> \033[01;37m''')

    if Tool == "0":
      all()
    elif Tool == "1":
      tmn()
    elif Tool == "2":
      cate()
    elif Tool == "3":
      tos()
    elif Tool == "4":
      Upt()
    elif Tool == "5":
      about()
    elif Tool == "rm -T" or Tool == "Uninstall Tool-X" or Tool == "uninstall tool-x" or Tool == "uninstall Tool-X" or Tool == "Uninstall tool-x":
      if system=="ubuntu":
        os.system("cd "+home+" && sudo rm -rf .Tool-X")
        os.system("cd "+bpath+" && sudo rm -rf Tool-X toolx")
      else:
        os.system("cd "+home+" && rm -rf .Tool-X")
        os.system("cd "+bpath+" && rm -rf Tool-X toolx")
      exit()
    elif Tool == "exit":
      exit()
    elif Tool == "x" or Tool=="X":
      Toolo = raw_input("\033[1;33m Do you want to Exit ? [Y/n] >  \033[01;33m")
      if Toolo == "N" or Toolo == "n":
        term()
        # make Y option default option
      elif Toolo == "Y" or Toolo == "y" or Toolo == "":
        exit()
      else:
        print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
        sleep(1)
        term()
    else:
      print ("\033[01;34m\007\n error : \033[01;37m\'"+Tool+"\' \033[01;31minvalid option !!!")
      sleep(1)
      term()

def ubu():
  while True:
    ux()
    menu()
    Tool = raw_input('''\033[1;36m
 ##> \033[01;37m''')
# is better to use switch statements in this cases
    if Tool == "0":
      all()
    elif Tool == "1":
      tmn()
    elif Tool == "2":
      cate()
    elif Tool == "3":
      Upt()
    elif Tool == "4":
      about()
    elif Tool == "rm -T" or Tool == "Uninstall Tool-X" or Tool == "uninstall tool-x" or Tool == "uninstall Tool-X" or Tool == "Uninstall tool-x":
      if system=="ubuntu":
        os.system("cd "+home+" && sudo rm -rf .Tool-X")
        os.system("cd "+bpath+" && sudo rm -rf Tool-X toolx")
      else:
        os.system("cd "+home+" && rm -rf .Tool-X")
        os.system("cd "+bpath+" && rm -rf Tool-X toolx")
      exit()
    elif Tool == "exit":
      exit()
    elif Tool == "x" or Tool=="X":
      Toolo = raw_input("\033[1;33m Do you want to Exit ? [Y/n] >  \033[1;m")
      if Toolo == "N" or Toolo == "n":
        ubu()
        # make Y option default
        elif Toolo == "Y" or Toolo == "y" or Toolo == "":
        exit()
      else:
        print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
        sleep(1)
        ubu()
    else:
      print ("\033[01;34m\007\n error : \033[01;37m\'"+Tool+"\' \033[01;31minvalid option !!!")
      sleep(1)
      ubu()

def ToolX():
  if system=="termux":
    term()
  else:
    ubu()
