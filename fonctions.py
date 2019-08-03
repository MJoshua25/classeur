import base64
import os

def get_mac():
    ipconfig = os.popen('getmac').readlines()
    mac = ""
    ligne=ipconfig[4]
    mac += ligne.split(' ')[0].strip() + "\n"
    return mac

def get_li(mac):
    li=(base64.b16encode(mac.encode("ascii"))).decode("utf-8")
    return li