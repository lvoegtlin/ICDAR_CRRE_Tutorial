FROM continuumio/anaconda3
COPY environment.yml environment.yml
RUN /bin/bash -c "source ~/.bashrc && conda env create -f environment.yml"
RUN mkdir /src
COPY binarize_manager.py /src/binarize_manager.py
RUN echo "source activate ICDAR_Tutorial" > ~/.bashrc
ENV PATH /opt/conda/envs/ICDAR_Tutorial/bin:$PATH
WORKDIR /src