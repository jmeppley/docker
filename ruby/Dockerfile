FROM joshuacook/base

MAINTAINER Joshua Cook <me@joshuacook.me>

USER root

# Ruby dependencies
RUN apt-get install -y --no-install-recommends ruby ruby-dev libtool autoconf automake gnuplot-nox libsqlite3-dev libatlas-base-dev libgsl0-dev libmagick++-dev imagemagick && \
    apt-get clean
RUN gem install --no-rdoc --no-ri sciruby-full

# Now switch to jovyan for all conda and other package manager installs
USER jovyan

# IRuby
RUN iruby register
