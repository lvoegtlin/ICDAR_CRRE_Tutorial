FROM continuumio/anaconda3

# copy environment file and install conda environment
COPY environment.yml environment.yml
RUN /bin/bash -c "source ~/.bashrc && conda env create -f environment.yml"

# copy method and start script
RUN mkdir /input
COPY binarize.py /input/binarize.py
COPY script.sh /input/script.sh

# activate env (put it into path for outorun)
RUN echo "source activate ICDAR_Tutorial" > ~/.bashrc
ENV PATH /opt/conda/envs/ICDAR_Tutorial/bin:$PATH

WORKDIR /input