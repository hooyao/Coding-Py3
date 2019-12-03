FROM codercom/code-server:v2
LABEL author="Hu Yao <hooyao@gmail.com>"

USER root
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV CONDA_BIN=https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh

RUN echo -e "\
channels: \n\
  - defaults \n\
show_channel_urls: true \n\
default_channels: \n\
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \n\
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free \n\
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r \n\
custom_channels: \n\
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \n\
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \n\
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \n\
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \n\
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \n\
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud \
" > ~/.condarc

RUN echo -e "\
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse\
" > /etc/apt/sources.list
RUN cat /etc/apt/sources.list
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

USER coder
