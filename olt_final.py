#!/usr/bin/env python

from __future__ import print_function
import jinja2
import yaml
from pprint import  pprint
import datetime
import re
import sys
import ipaddress
reload(sys)
sys.setdefaultencoding('utf8')
date = datetime.datetime.now().strftime("%y-%m-%d")
print ('Please pick an option')             
my_dict = {}

##############################################################################
#########            Function to Render Jinja File                ############
##############################################################################
def build_template(template_file, my_vars, date = "date"):
    with open(template_file) as f1:
        config_file = f1.read()
        print (date)
        #print (config_file)
        f1.close
    with open(my_vars) as f2:
        var_file = yaml.load(f2)
        f2.close
    file = jinja2.Template(config_file)
    var_file['date']=date
    cfg_output = file.render(var_file)
    return cfg_output

def build_template2(template_file):
    with open(template_file) as f1:
        config_file = f1.read()
        #print (config_file)
        f1.close
    file = jinja2.Template(config_file)
    cfg_output = file.render(my_dict)
    return cfg_output

choice = eval(raw_input('Type 1 for NEW OLT, Type 2 for CARD ADD: '))
#print ("~"+choice+"~")
if choice == 1:
    cfg_output = build_template("OLT_config.j2","olt.yml", date)
    print (cfg_output)
else:
    card = raw_input('Which Line CARD is being installed (1-14):  ')
    ip_addr1 = raw_input('What is the IP address of the OLT:  ')
    cfg_output = build_template2("card_add.j2")
    my_dict = {"card":card, "ip_addr1":ip_addr1}
    cfg_output = build_template2("card_add.j2")
    print (cfg_output)
    
    
    
    
