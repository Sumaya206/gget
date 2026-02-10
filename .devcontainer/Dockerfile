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

# Configure conda channels: use conda-forge and bioconda only (no defaults/Anaconda TOS needed)
RUN conda config --remove channels defaults 2>/dev/null; \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --set channel_priority strict

# Core scientific Python stack via conda
RUN conda install -y -c conda-forge -c bioconda --override-channels \
        numpy \
        pandas \
        matplotlib \
    && conda clean -afy

# PyPI packages via pip
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install \
        gget \
        requests \
    && pip cache purge