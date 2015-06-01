#!/usr/bin/env python

import logging
from resource_management import *

config = Script.get_config()

hostname = config['public_hostname']

app_conf_dir = config['configurations']['global']['app_conf_dir']
user = config['configurations']['global']['user']
group = config['configurations']['global']['group']
pid_file = config['configurations']['global']['pid_file']

start_command = config['configurations']['global']['start_command']

httpfs_site = config['configurations']['httpfs-site']

