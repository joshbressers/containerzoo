FROM debian
ARG user
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y bsdgames cowsay irssi ca-certificates figlet vim x11-apps xmille
RUN useradd -m ${user}
ENV PATH ${PATH}:/usr/games/
