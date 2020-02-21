#
#                                 - [ BROAD'20 ] -
#
# A docker instance for accessing AWS resources
# This wraps the fiji docker registry
#

FROM fiji/fiji:fiji-openjdk-8

# Install S3FS 

RUN sudo apt-get -y update           && \
    sudo apt-get -y upgrade          && \
    sudo apt-get -y install 		\
	automake 		\
	autotools-dev 		\
	g++ 			\
	git 			\
	libcurl4-gnutls-dev 	\
	libfuse-dev 		\
	libssl-dev 		\
	libxml2-dev 		\
	make pkg-config		\
	sysstat			\
	curl

WORKDIR /usr/local/src
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git
WORKDIR /usr/local/src/s3fs-fuse
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

# Install AWS CLI

RUN \
  pip install awscli 

# Install boto3

RUN \
  pip install -U boto3

# Install watchtower for logging

RUN \
  pip install watchtower

# SETUP NEW ENTRYPOINT

RUN mkdir -p /home/ubuntu/
WORKDIR /home/ubuntu
COPY fiji-worker.py .
COPY instance-monitor.py .
COPY run-worker.sh .
RUN chmod 755 run-worker.sh

ENTRYPOINT ["./run-worker.sh"]
CMD [""]

