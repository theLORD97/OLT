#!/usr/bin/env python

from __future__ import print_function
import jinja2
import yaml
from pprint import  pprint
from datetime import datetime
import datetime
import re
import sys
import ipaddress
#sys.setdefaultencoding('utf-8')


date = datetime.datetime.now().strftime("%y-%m-%d")

##############################################################################
#########            Function to Verify IP address                ############
##############################################################################
def ip_checkv4(ip):
    parts=ip.split(".")
    if len(parts)<4 or len(parts)>4:
        return "Invalid IP length, do you even know what you're doing??? "
    else:
         while len(parts)== 4:
            a=int(parts[0])
            b=int(parts[1])
            c=int(parts[2])
            d=int(parts[3])
            if a<= 0 or a == 127 :
                return "invalid IP address"
            elif d == 0:
                return "host id should not be 0 or less than zero " 
            elif a>=255:
                return "1st octet is invalid - go back to school"
            elif b>=255 or b<0: 
                return "2nd octet is invalid - are you even paying attention? "
            elif c>=255 or c<0:
                return "Thrid octet is invalid - Strike 3 "
            elif d>=255 or c<0:
                return "YOU'RE FIRED"
            else:
                return "Valid IP address"
                

##############################################################################
#########            Function to Render Jinja File                ############
##############################################################################
def build_template(template_file):
    with open(template_file) as f1:
        config_file = f1.read()
        #print (config_file)
        f1.close
    file = jinja2.Template(config_file)
    cfg_output = file.render(my_dict)
    return cfg_output


########################## IP address Error Check  ############################
while True:
    ip_addr1 = raw_input('MGMT IP Addreess:  ')
    result = (ip_checkv4(ip_addr1))
    print (result)
    if result == "Valid IP address":
        break

########################## IP address 2 Error Check  ########################## 
while True:
    ip_addr2 = raw_input('GW address:  ') 
    result = (ip_checkv4(ip_addr2))
    print (result)
    if result == "Valid IP address":
        break
    

############################# Input LER ports  ################################
upstream_fqdn = raw_input('Upstream POP FQDN: ')
upstream_port = raw_input('Remote LER port number:  ')
fqdn = raw_input('Hostname:  ')
card = raw_input('How many line cards are being installed (1-14):   ')
pop_name = raw_input('POP Name  (ex Drayton Valley):  ')



my_dict = {"upstream_fqdn":upstream_fqdn, "upstream_port":upstream_port, "ip_addr1":ip_addr1, "ip_addr2":ip_addr2, "fqdn":fqdn, "date":date, "card":card, "pop_name":pop_name}
#print (my_dict)
print ("\n\n")    
 
cfg_output = build_template("OLT_config.j2")
print (cfg_output)


