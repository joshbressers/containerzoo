#!/usr/bin/env python3

import sys
import os
import subprocess

homedir=os.path.join(os.getenv("HOME"), 'docker-home:/home/container')

the_command = os.path.basename(sys.argv[0])
print(the_command)

# docker run --rm -i -v $HOME/docker-home:/home/container -u container -t linux-commands $command $@
#

cmd = ['docker', 'run', '--rm', '-i', '-v', homedir, '-u', 'container', '-t',
'linux-commands', the_command]
cmd.extend(sys.argv[1:])
output = subprocess.run(cmd)
