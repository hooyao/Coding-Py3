FROM codercom/code-server:v2
LABEL author="Hu Yao <hooyao@gmail.com>"

USER root
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV CONDA_BIN=https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh

COPY .condarc  /root/.condarc
COPY sources.list /etc/apt/sources.list
RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL ${CONDA_BIN} -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && apt-get -qq -y remove bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes
ENV PATH /opt/conda/bin:$PATH

RUN conda install -y python=3.7 && \
    conda install numpy pandas cython scikit-learn scipy matplotlib sympy -y &&\
    conda clean -a && \
    rm -rf /opt/conda/pkgs/*
