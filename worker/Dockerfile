#
#                                 - [ BROAD'20 ] -
#
# A docker instance for accessing AWS resources
# This wraps the fiji docker registry
#

FROM fiji/fiji:fiji-openjdk-8

USER root

# Install S3FS

RUN apt-get -y update           && \
    apt-get -y upgrade          && \
    apt-get -y install 		\
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

RUN apt-get -y upgrade python2.7
RUN apt-get -y install python-pip

RUN \
  pip install awscli

# Install boto3

RUN \
  pip install -U boto3

# Install watchtower for logging

RUN \
  pip install watchtower

# SETUP NEW ENTRYPOINT

WORKDIR /opt/fiji
COPY fiji-worker.py .
COPY instance-monitor.py .
COPY run-worker.sh .
RUN chmod 755 run-worker.sh

ENTRYPOINT ["./run-worker.sh"]
CMD [""]
