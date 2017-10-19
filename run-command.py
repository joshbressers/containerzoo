#!/usr/bin/env python3

import sys
import os
import subprocess
import select

stdin_data = False

if select.select([sys.stdin,],[],[],0.0)[0]:
    stdin_data = True

homedir=os.path.join(os.getenv("HOME"), 'docker-home:/home/container')

the_command = os.path.basename(sys.argv[0])


# XXX: I'm unsure if we can do this nicely with docker, if we claim a tty,
# we can't pipe from stdin
if stdin_data:
    # We have data waiting on stdin
    cmd = ['docker', 'run', '--rm', '-a', 'stdin', '-a', 'stdout', '-a', 'stderr', '-i', '-v', homedir, '-u', 'container', 'linux-commands', the_command]
else:
    # Nothing is waiting on stdin, we can grab a terminal
    cmd = ['docker', 'run', '--rm', '-a', 'stdin', '-a', 'stdout', '-a', 'stderr', '-i', '-v', homedir, '-u', 'container', '-t', 'linux-commands', the_command]

cmd.extend(sys.argv[1:])

# Let's look if the last command is a file or directory
# XXX: Not every command will do this, for now let's guess

full_path = None
if len(sys.argv[1:]) > 0:
    if os.path.exists(sys.argv[-1]):
        full_path = os.path.abspath(sys.argv[-1])

        if os.path.islink(full_path):
            # symlinks are hard, let's give up
            pass
        else:
            cmd.insert(2, "-v")
            cmd.insert(3, "%s:%s" % (full_path, full_path))

os.execve('/usr/local/bin/docker', cmd, os.environ)
