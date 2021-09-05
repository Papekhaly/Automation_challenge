FROM jenkins/jenkins:lts

USER root
#copy requirements

COPY requirements.txt  / 

#install python3.9
    
RUN apt-get update && apt-get install -y python3.9 

# Add 3.9 to the available alternatives
#RUN update-alternatives --install /usr/bin/python3.9 python /usr/bin/python3.9 1

# Set python3.9 as the default python
#RUN update-alternatives --set python /usr/bin/python3.9

ENV JENKINS_OPTS --prefix=/jenkins/ 

#install requirement
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt

# Install Ansible
RUN apt-get update && \
    apt-get -y install ansible

# Install the latest Docker CE binaries
RUN apt-get update && \
    apt-get -y install apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable" && \
   apt-get update && \
   apt-get -y install docker-ce docker-ce-cli containerd.io
