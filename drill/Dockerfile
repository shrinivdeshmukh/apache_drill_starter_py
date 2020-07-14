FROM openjdk:8

RUN apt-get update -y; apt-get install wget -y

RUN cd /tmp && wget https://downloads.apache.org/drill/drill-1.17.0/apache-drill-1.17.0.tar.gz

RUN cd /tmp; tar xzf apache-drill-1.17.0.tar.gz; mv apache-drill-1.17.0 /usr/local/drill

COPY drill-override.conf /usr/local/drill/conf/drill-override.conf

WORKDIR /usr/local/drill