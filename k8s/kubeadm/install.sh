#!/bin/bash
set -e

ROLE=$1

if [[ "$ROLE" != "master" && "$ROLE" != "worker" ]]; then
  echo "Usage: sudo bash install.sh [master|worker]"
  exit 1
fi

echo "===== Kubernetes $ROLE setup started ====="

### Disable swap
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab

### Kernel modules
cat <<EOF >/etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter

cat <<EOF >/etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

sysctl --system

### Install Docker
apt update
apt install -y ca-certificates curl gnupg

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg |
gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" \
> /etc/apt/sources.list.d/docker.list

apt update
apt install -y docker-ce docker-ce-cli containerd.io

cat <<EOF >/etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "storage-driver": "overlay2"
}
EOF

systemctl daemon-reexec
systemctl restart docker
systemctl enable docker

### Install cri-dockerd
VERSION="0.3.15"
curl -LO https://github.com/Mirantis/cri-dockerd/releases/download/v${VERSION}/cri-dockerd_${VERSION}.3-0.ubuntu-jammy_amd64.deb
dpkg -i cri-dockerd_${VERSION}.3-0.ubuntu-jammy_amd64.deb

systemctl enable cri-docker.service
systemctl enable --now cri-docker.socket

### Install Kubernetes tools
apt update
apt install -y apt-transport-https ca-certificates curl

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key |
gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" \
> /etc/apt/sources.list.d/kubernetes.list

apt update
apt install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl

### MASTER SETUP
if [ "$ROLE" = "master" ]; then
  echo "===== Initializing Control Plane ====="
  kubeadm init \
    --pod-network-cidr=192.168.0.0/16 \
    --cri-socket unix:///var/run/cri-dockerd.sock

  mkdir -p $HOME/.kube
  cp /etc/kubernetes/admin.conf $HOME/.kube/config
  chown $(id -u):$(id -g) $HOME/.kube/config

  echo "===== Installing Calico ====="
  kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml

  echo "====================================="
  echo "✔ MASTER READY"
  echo "👉 COPY kubeadm join command above"
  echo "====================================="
fi

echo "===== Kubernetes $ROLE setup completed ====="
