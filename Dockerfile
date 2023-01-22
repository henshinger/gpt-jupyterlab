FROM jupyter/scipy-notebook

LABEL maintainer="Kenley Tan <kenley.tan@hey.com>"

# Install pyarrow
RUN mamba install --quiet --yes \
    'pyarrow' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
