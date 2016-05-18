FROM joshuacook/base

MAINTAINER Joshua Cook <me@joshuacook.me>

# Configure environment
ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV SHELL /bin/bash
ENV NB_USER jovyan
ENV NB_UID 1000

# Create jovyan user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p /opt/conda && \
    chown jovyan /opt/conda

# Install Jupyter notebook
RUN conda install --quiet --yes \
    'notebook=4.1*' \
    terminado \
    && conda clean -tipsy

USER jovyan

# Setup Jovyan home directory
RUN mkdir /home/$NB_USER/work && \
    mkdir /home/$NB_USER/.jupyter && \
    mkdir /home/$NB_USER/.local && \
    echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$NB_USER/.curlrc

USER root

# Configure container startup as root
EXPOSE 8888
WORKDIR /home/$NB_USER/work
ENTRYPOINT ["/tini", "--"]
CMD ["/start-notebook.sh"]

# Add local files as late as possible to avoid cache busting
# Start notebook server
COPY start-notebook.sh /start-notebook.sh
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter
RUN chmod +x /start-notebook.sh

# Switch back to jovyan to avoid accidental container runs as root
USER jovyan
