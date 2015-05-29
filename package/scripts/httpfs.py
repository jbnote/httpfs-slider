#!/usr/bin/env python

import os
from resource_management import *

import logging

logger = logging.getLogger()

class HTTPFS(Script):
  def install(self, env):
    import params
    env.set_params(params)
    self.install_packages(env)


  def configure(self, env):
    import params
    env.set_params(params)

    Directory(params.app_conf_dir)

    File(params.app_conf_dir + '/httpfs-site.xml',
         content = Template('httpfs-site.xml.j2'),
         owner = params.user,
         group = params.group)

    File(params.app_conf_dir + '/httpfs-env.sh',
         content = StaticFile('httpfs-env.sh'),
         owner = params.user,
         group = params.group)

    File(params.app_conf_dir + '/httpfs-log4j.properties',
         content = StaticFile('httpfs-log4j.properties'),
         owner = params.user,
         group = params.group)


  def start(self, env):
    import params
    env.set_params(params)
    self.configure(env)
    Execute(params.start_command,
            logoutput = True,
            wait_for_finish = False,
            pid_file = params.pid_file,
            poll_after = 5)


  def status(self, env):
    import params
    env.set_params(params)
    check_process_status(params.pid_file)


if __name__ == "__main__":
  HTTPFS().execute()

