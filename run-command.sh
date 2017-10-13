#!/bin/sh

command=`basename $0`

# Docker commands
#COMMANDS=(robots mille cowsay cribbage snake rain irssi figlet rot13)
#for x in $COMMANDS; do
#alias $x="docker run --rm -i -v /Users/bress/docker-home:/home/bress -u bress -t linux-commands $x"
#done
##alias docker-shell="docker run --rm -i -v /Users/bress/docker-home:/home/bress -u bress -t linux-commands bash"

docker run --rm -i -v $HOME/docker-home:/home/container -u container -t linux-commands $command $@
