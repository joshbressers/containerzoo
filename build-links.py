#!/usr/bin/env python3

import os
import sys
import subprocess

# Things in the container I want to link. These must be in the default path
#/usr/games/
#irssi

commands = ["irssi", "bash", "vi", "xeyes", "xlogo", "xmille"]
paths = ["/usr/games"]

# Directories of stuff
for x in paths:
    cmd = ['docker', 'run', '--rm', '-u', 'container', '-t', 'linux-commands', 'find', x, '-type', 'f']
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    files = output.stdout.readlines()
    for i in files:
        the_name = i.decode('utf-8')
        docker_file = os.path.basename(the_name.rstrip())
        commands.append(docker_file)

for i in commands:
    the_command = "commands/%s" % i
    try:
        # Does the file exist?
        os.stat(the_command)
        # Remove it if it's there
        if os.path.islink(the_command):
            os.unlink(the_command)
        else:
            # Something horrible has happened
            print("%s isn't a symlink, exiting" % the_command)
            sys.exit(1)
    except FileNotFoundError:
        pass

    os.symlink("../run-command.py", the_command)
