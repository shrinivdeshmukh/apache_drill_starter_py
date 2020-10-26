FROM openjdk:8

RUN apt-get update -y

WORKDIR /tmp

RUN wget https://www-us.apache.org/dist/hadoop/common/hadoop-2.10.0/hadoop-2.10.0.tar.gz

RUN tar xzf hadoop-2.10.0.tar.gz

RUN mv hadoop-2.10.0 /usr/local/hadoop

COPY *.yaml /usr/local/hadoop/etc/hadoop/

RUN apt-get install openssh-server -y

RUN mkdir /var/run/sshd

COPY hadoop-env.sh /usr/local/hadoop/etc/hadoop/

COPY hdfs-site.xml /usr/local/hadoop/etc/hadoop/hdfs-site.xml

COPY core-site.xml /usr/local/hadoop/etc/hadoop/core-site.xml

COPY mapred-site.xml /usr/local/hadoop/etc/hadoop/mapred-site.xml

COPY yarn-site.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml

COPY entrypoint.sh /usr/local/hadoop/

COPY ssh_config /root/.ssh/config
# RUN apt-get -y install sudo

# RUN useradd -ms /bin/bash shrinivasdeshmukh && echo "shrinivasdeshmukh:shrinivasdeshmukh" | chpasswd && adduser shrinivasdeshmukh root

# USER shrinivasdeshmukh

RUN /usr/local/hadoop/bin/hdfs namenode -format

WORKDIR /usr/local/hadoop

COPY test.csv data.json /tmp/

CMD ["bash", "entrypoint.sh"]
