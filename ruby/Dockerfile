FROM joshuacook/minimal-notebook

MAINTAINER Joshua Cook <me@joshuacook.me>

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && \
    apt-get install -yq \
    python3 \
    python3-dev \
    python3-pip \
    libzmq3 \
    libzmq3-dev \
    zlib1g-dev \
    libssl-dev \
    libreadline-dev \
    && apt-get clean && \
    ln -s /usr/bin/libtoolize /usr/bin/libtool

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools && \
    apt-get clean

# Provision scipy/numpy
RUN conda install --yes \
    'ipywidgets=4.1*' \
    'pandas=0.17*' \
    'matplotlib=1.5*' \
    'scipy=0.17*' \
    'seaborn=0.7*' \
    'scikit-learn=0.17*' \
    'scikit-image=0.11*' \
    'sympy=0.7*' \
    'cython=0.23*' \
    'patsy=0.4*' \
    'statsmodels=0.6*' \
    'cloudpickle=0.1*' \
    'dill=0.2*' \
    'numba=0.23*' \
    'bokeh=0.11*' \
    'h5py=2.5*' \
    && conda clean -tipsy

# Set the Ruby version of your preference
ENV RUBY_VERSION 2.2.2

RUN echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\
    mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-build.git &&\
    cd /src/ruby-build && ./install.sh &&\
    cd / && rm -rf /src/ruby-build && ruby-build $RUBY_VERSION /usr/local

RUN gem update --system

RUN gem install nmatrix -v 0.2.0

RUN gem install --no-rdoc --no-ri sciruby iruby

RUN gem install ffi-rzmq

# omoikane mixed_models nmatrix-lapacke mikon spreadsheet statsample daru

RUN gem install rubygems-update

#RUN apt-get update && \
#    apt-get install -yq \
#    qt5-default \
#    libqt5webkit5-dev \
#    gstreamer1.0-plugins-base \
#    gstreamer1.0-tools \
#    gstreamer1.0-x \
#    && apt-get clean

#RUN gem install --no-rdoc --no-ri \
#    capybara \
#    capybara-screenshot \
#    poltergeist \
#    rest-client \
#    rspec \
#    selenium-webdriver

RUN gem install \
  activesupport \
  airborne \
  byebug \
  eventmachine \
  faye-websocket \
  httparty \
  json_expressions \
  koala \
  nokogiri \
  rest-client \
  rspec \
  sinatra \
  twitter

RUN conda install -c jjhelmus --yes feather-format=0.1.0

RUN gem install awesome_print

USER jovyan

# IRuby
RUN iruby register
