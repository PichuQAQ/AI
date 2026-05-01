# Runbook: Linux Filesystem Usage High

## Symptom
Grafana alert: filesystem usage above 85% or 95%.

## Impact
If `/` is full, services may fail:
- VS Code Remote-SSH
- Cockpit
- PackageKit
- systemd services
- Docker logs

## Check current usage

```bash
df -h
df -i
sudo du -xhd1 / | sort -hr
sudo du -xhd1 /var | sort -hr
sudo du -xhd1 /home | sort -hr

docker system df
sudo du -sh /var/lib/docker

sudo apt clean
sudo journalctl --vacuum-time=7d
docker system prune
