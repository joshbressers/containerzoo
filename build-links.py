#!/usr/bin/env python3

import os
import subprocess

# Things in the container I want to link. These must be in the default path
#/usr/games/
#irssi

commands = ["irssi", "ls", "bash"]
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
    os.symlink("../run-command.sh", "commands/%s" % i)
