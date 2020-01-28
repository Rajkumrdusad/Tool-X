import os
import sys
try:
  import requests
except:
  os.system("pip install requests")
  os.system("pip3 install requests")

class sys:
  pac=None
  sys=None
  home=os.getenv("HOME")
  bin=None
  sudo=None
  connection=False
  conf_dir=None
  def __init__(self):
    try:
      if requests.get("https://www.google.com").ok:
        self.connection=True
    except:
      self.connection=False

    if os.path.exists("/usr/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/bin/sudo"):
      self.sudo="sudo"

    if os.path.exists("/usr/etc"):
      self.conf_dir="/usr/etc"
    elif os.path.exists("/data/data/com.termux/files/usr/etc"):
      self.conf_dir="/data/data/com.termux/files/usr/etc"
    elif os.path.exists("/etc"):
      self.conf_dir="/etc"

    if os.path.exists("/usr/bin/yum"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="yum"
    elif os.path.exists("/usr/bin/apt"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apt-get"
    elif os.path.exists("/bin/apt"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apt-get"
    elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
      self.sys="linux"
      self.bin="/data/data/com.termux/files/usr/bin"
      self.pac="pkg"
    elif os.path.exists("/usr/bin/brew"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="brew"
    elif os.path.exists("/bin/brew"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="brew"
    elif os.path.exists("/sbin/apk"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apk"
