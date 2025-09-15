FROM scoringengine/base

USER root

RUN \
  apt-get update && \
  # apt-get install -y apt-transport-https software-properties-common
  apt-get install -y apt-transport-https gpg

# ICMP Check
RUN apt-get install -y iputils-ping

# HTTP/S Check
RUN apt-get install -y curl

# MySQL Check
RUN apt-get install -y default-mysql-client

# LDAP Check
RUN apt-get install -y ldap-utils

# VNC Check
RUN apt-get install -y medusa

# SSH Check
# RUN pip install -I "cryptography>=3.4,<3.5"
RUN pip install "paramiko==3.5.0"

# WinRM Check
RUN pip install -I "pywinrm>=0.5.0,<0.6"

# Elasticsearch Check
RUN pip install -I "requests>=2.32.3,<2.33"

# SMB Check
RUN pip install -I "pysmb>=1.2,<1.3"

# DNS Check
RUN apt-get install -y dnsutils

# Postgresql Check
RUN apt-get install -y postgresql-client

# RDP Check
RUN apt-get update && apt-get install -y freerdp3-x11
RUN apt-get install -y xvfb

# Telnet Check
RUN pip install -I "telnetlib3==1.0.1"

# OpenVPN Check
RUN apt-get install -y openvpn iproute2 sudo

RUN rm -rf /var/lib/apt/lists/*

COPY bin/worker /app/bin/worker
COPY docker/worker/sudoers /etc/sudoers

USER root

COPY scoring_engine /app/scoring_engine
RUN chmod +x /app/scoring_engine/checks/bin/nfs_check
RUN pip install -e .

CMD ["./wait-for-port.sh", "redis:6379", "/app/bin/worker"]