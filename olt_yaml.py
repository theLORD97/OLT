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
reload(sys)
sys.setdefaultencoding('utf8')
date = datetime.datetime.now().strftime("%y-%m-%d")
                

##############################################################################
#########            Function to Render Jinja File                ############
##############################################################################
def build_template(template_file, my_vars):
    with open(template_file) as f1:
        config_file = f1.read()
        #print (config_file)
        f1.close
    with open(my_vars) as f2:
        var_file = yaml.load(f2)
        f2.close
    file = jinja2.Template(config_file)
    cfg_output = file.render(var_file)
    return cfg_output


cfg_output = build_template("OLT_config.j2","olt.yml")
print (cfg_output)


