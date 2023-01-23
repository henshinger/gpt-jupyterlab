FROM jupyter/scipy-notebook

LABEL maintainer="Kenley Tan <kenley.tan@hey.com>"

# Install pyarrow
RUN pip install gpt_jupyterlab