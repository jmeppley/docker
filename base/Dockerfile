FROM debian

MAINTAINER Joshua Cook <me@joshuacook.me>

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get install -yq --no-install-recommends \
  build-essential \
  bzip2 \
  ca-certificates \
  emacs \
  git \
  jed \
  libsm6 \
  libxrender1 \
  locales \
  pandoc \
  python-dev \
  sudo \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-fonts-extra \
  texlive-fonts-recommended \
  texlive-generic-recommended \
  unzip \
  vim \
  wget \
  && apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh && \
    /bin/bash /Miniconda3-4.0.5-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-4.0.5-Linux-x86_64.sh

ARG TINI_VERSION=v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

RUN apt-get update -qq \
  && apt-get install -y locales -qq \
  && locale-gen en_US.UTF-8 en_us \
  && dpkg-reconfigure locales \
  && dpkg-reconfigure locales \
  && locale-gen C.UTF-8 \
  && /usr/sbin/update-locale LANG=C.UTF-8
  
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

ENTRYPOINT ["/tini", "--"]
