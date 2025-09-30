FROM jrei/systemd-ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# SSH + utilitaires
RUN apt-get update && apt-get install -y openssh-server sudo curl git nginx python3 python3-venv python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# SSH root par clé uniquement
RUN mkdir -p /var/run/sshd /root/.ssh && chmod 700 /root/.ssh && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config
COPY authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

# Activer ssh au boot systemd
RUN systemctl enable ssh

EXPOSE 22
CMD ["/sbin/init"]
