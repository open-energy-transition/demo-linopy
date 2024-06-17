FROM condaforge/mambaforge

RUN conda update -n base conda
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba

COPY . .

RUN conda env create -f env.yaml

RUN echo "source activate linotest" > ~/.bashrc
ENV PATH /opt/conda/envs/linotest/bin:$PATH

ENTRYPOINT [ "python" , "execute.py" ]

# docker build -t linotest .
# sudo docker run -it --entrypoint /bin/bash linotest
# docker run --name democontainer -v "$(pwd)"/input:/input -v "$(pwd)"/result:/result





