FROM joshuacook/datascience

MAINTAINER Joshua Cook <me@joshuacook.me>

USER root

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Julia dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    julia \
    libnettle4 && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jovyan

# Install IJulia packages as jovyan and then move the kernelspec out
# to the system share location. Avoids problems with runtime UID change not
# taking effect properly on the .local folder in the jovyan home dir.
RUN julia -e 'Pkg.add("IJulia")' && \
    mv /home/$NB_USER/.local/share/jupyter/kernels/* $CONDA_DIR/share/jupyter/kernels/ && \
    chmod -R go+rx $CONDA_DIR/share/jupyter && \
    rm -rf /home/$NB_USER/.local/share

# Show Julia where conda libraries are
# Add essential packages
RUN echo 'push!(Sys.DL_LOAD_PATH, "/opt/conda/lib")' > /home/$NB_USER/.juliarc.jl && \
    julia -e 'Pkg.add("Gadfly")'  && \
    julia -e 'Pkg.add("RDatasets")' && \
    julia -F -e 'Pkg.add("HDF5")' && \
    julia -e 'Pkg.add("Match")'
