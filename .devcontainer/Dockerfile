FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# use this Dockerfile to install additional tools you might need, e.g.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Install Miniconda (Linux)
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --no-install-recommends \
        wget \
        ca-certificates \
        bzip2 \
    && rm -rf /var/lib/apt/lists/*

ARG TARGETARCH
RUN set -eux; \
    if [ "${TARGETARCH}" = "arm64" ]; then \
      MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py311_24.7.1-0-Linux-aarch64.sh"; \
    else \
      MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-py311_24.7.1-0-Linux-x86_64.sh"; \
    fi; \
    wget -q "$MINICONDA_URL" -O /tmp/miniconda.sh; \
    bash /tmp/miniconda.sh -b -p "$CONDA_DIR"; \
    rm /tmp/miniconda.sh

# Force conda to use the stable classic solver to avoid libarchive errors
RUN conda config --set solver classic

# Configure conda channels: use conda-forge and bioconda only (no defaults/Anaconda TOS needed)
RUN conda config --remove channels defaults 2>/dev/null; \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --set channel_priority strict

# Core scientific Python stack via conda (Added Python pin)
RUN /opt/conda/bin/conda install -y -c conda-forge -c bioconda --override-channels \
        python=3.11 \
        numpy=2.1 \
        pandas=2.2 \
        matplotlib=3.9 \
        scipy=1.14 \
        biopython=1.84 \
        openssl \
    && /opt/conda/bin/conda clean -afy


# PyPI packages via pip (Fixed to double equals ==)
RUN /opt/conda/bin/python -m pip install --upgrade pip setuptools wheel && \
    /opt/conda/bin/pip install \
        gget==0.30.2 \
        requests==2.32.3 \
    && /opt/conda/bin/pip cache purge

# Add gget setup script
RUN /opt/conda/bin/python -c "import gget; gget.setup('elm')"